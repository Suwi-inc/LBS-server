import logging
from datetime import datetime, timedelta
from .. import db
from ..model.models import LOGS
from ..utils.route_information import RouteInfo

# Logging module which logs errors and requests logs to the provided logging db


class SQLAlchemyHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)

    def emit(self, record):
        log_entry = LOGS(
            module=record.name,
            log_type=record.levelname,
            message=record.msg if hasattr(record, "msg") else "",
            endpoint=record.endpoint if hasattr(record, "endpoint") else "",
            methods=record.methods if hasattr(record, "methods") else "",
            time=datetime.now(),
        )
        db.session.add(log_entry)
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

        # Database handler
        db_handler = SQLAlchemyHandler()
        db_handler.setLevel(logging.DEBUG)
        db_formatter = logging.Formatter(
            "%(name)s %(asctime)s %(levelname)s %(message)s"
        )
        db_handler.setFormatter(db_formatter)
        logger.addHandler(db_handler)

    return CustomLoggerAdapter(logger, {})


def log(logger, message, level, endpoint="", methods=""):
    """
    Log messages with various levels and extra context.

    Args:
        logger (logging.LoggerAdapter): The logger instance to use for logging.
        message (str): The message to be logged.
        level (str): The level of the log (e.g., "info", "warn", "error", "critical").
        endpoint (str, optional): The endpoint related to the log message. Default is an empty string.
        methods (str, optional): The HTTP methods related to the log message. Default is an empty string.
    """
    extra = {"endpoint": endpoint, "methods": methods}
    if level == "info":
        logger.info(message, extra=extra)
    elif level == "warn":
        logger.warning(message, extra=extra)
    elif level == "error":
        logger.error(message, extra=extra)
    elif level == "critical":
        logger.critical(message, extra=extra)
    else:
        logger.error(message, extra=extra)


# Function to log informational requests


def log_request(request: RouteInfo, message, module):
    """
    Log user requests.

    Args:
        request (RouteInfo): The request information which includes the endpoint route and the methods.
        message (str): The message to be logged.
        module (str) : The module or file where this action occured
        level (str): The level of the log (e.g., "info", "warn", "error", "critical").
        endpoint (str, optional): The endpoint related to the log message. Default is an empty string.
        methods (str, optional): The HTTP methods related to the log message. Default is an empty string.
    """
    logger = configure_logger(module)
    log(logger, message, "info", request.endpoint, request.methods)


# Function to log errors
def log_error(request: RouteInfo, error, module, level="error"):
    """
    Log errors and expetions.

    Args:
        request (RouteInfo): The request information which includes the endpoint (str)  and the methods (str).
        error (str): The error to be logged.
        module (str) : The module or file where this error occured
        level (str): The level of the log (e.g."warn", "error" or "critical").
    """
    logger = configure_logger(module)
    log(logger, error, level, request.endpoint, request.methods)


# Function to log warnings
def log_warning(request: RouteInfo, error, module):
    log_error(request, error, module, "warning")


# Function to log critical errors
def log_critical(request: RouteInfo, error, module):
    log_error(request, error, module, "critical")
