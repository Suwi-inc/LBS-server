import logging
from datetime import datetime, timezone

from .. import db
from ..model.models import Log, Position
from ..utils.data_objects import LocationInfo


# Logging module which logs errors and requests logs to the provided logging db
class SQLAlchemyHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        log_entry = Log(
            module=record.name,
            log_type=record.levelname,
            message=record.msg if hasattr(record, "msg") else "",
            endpoint=record.endpoint if hasattr(record, "endpoint") else "",
            methods=record.methods if hasattr(record, "methods") else "",
            device_id=(record.device_id if hasattr(record, "device_id") else ""),
            time=datetime.now(timezone.utc),
        )
        db.session.add(log_entry)
        db.session.flush()
        if record.location is not None:
            position_entry = Position(
                latitude=record.location.latitude,
                longitude=record.location.longitude,
                location_precision=record.location.precision,
                position_time=record.location.time,
                log_id=log_entry.id,
            )
            db.session.add(position_entry)
        db.session.commit()


class CustomLoggerAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        extra = self.extra.copy()
        extra.update(kwargs.get("extra", {}))
        return msg, {"extra": extra}


def configure_logger(module):
    """
    Configure the database custom logger

    Args:
        module (str) : The module or file where this action occured
    """
    logger = logging.getLogger(module)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        db_handler = SQLAlchemyHandler()
        db_handler.setLevel(logging.DEBUG)
        db_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        db_handler.setFormatter(db_formatter)
        logger.addHandler(db_handler)

    return CustomLoggerAdapter(logger, {})


def log(logger, level, message, endpoint, methods, device_id, location):
    """
    Log messages with various levels and extra context.

    Args:
        logger (logging.LoggerAdapter): The logger instance to use for logging.
        message (str): The message to be logged.
        level (str): The level of the log (e.g., "info", "warn", "error", "critical").
        endpoint (str, optional): The endpoint related to the log message. Default is an empty string.
        methods (str, optional): The HTTP methods related to the log message. Default is an empty string.
    """
    extra = {
        "endpoint": endpoint,
        "methods": methods,
        "device_id": device_id,
        "location": location,
    }
    print(level)
    if level == "info":
        logger.info(message, extra=extra)
    elif level == "warning":
        logger.warning(message, extra=extra)
    elif level == "error":
        logger.error(message, extra=extra)
    elif level == "critical":
        logger.critical(message, extra=extra)
    else:
        logger.error(message, extra=extra)


# Function to log errors and requests
def log_action(
    module,
    message,
    endpoint,
    methods,
    device_id,
    level="error",
    location: LocationInfo = None,
):
    """
    Log errors, expetions and requests.

    Args:
        endpoint (str) : The request endpoint.
        methods (str) : The request methods.
        device_id (str) : The device's identifier.
        message (str): The error or messageto be logged.
        module (str) : The module or file where this error occured
        level (str): The level of the log (e.g."info", "warning", "error" or "critical"). Default is error.
        location (LocationInfo): The calculated position of a device based on the cell tower data. Includes latitude,longitude,precision and time
    """
    logger = configure_logger(module)
    log(logger, level, message, endpoint, methods, device_id, location)
