import logging
from datetime import datetime, timedelta

today_date = datetime.now().strftime("%Y-%m-%d")


def configure_logger(module, log_file):
    logger = logging.getLogger(module)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(log_file, mode="a")
        formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


def log(logger, message, level):
    if level == "info":
        logger.info(message)
    elif level == "warn":
        logger.warning(message)
    elif level == "error":
        logger.error(message)
    elif level == "critical":
        logger.critical(message)


def log_request(request, message, module):
    log_file = f"requests_{today_date}.log"
    logger = configure_logger(module, log_file)
    log(logger, f"{request} : {message}", "info")


def log_error(endpoint, error, module, level):
    log_file = f"errors_{today_date}.log"
    logger = configure_logger(module, log_file)
    log(logger, f"{endpoint} : {error}", level)
