import logging
import os
from datetime import datetime
from app.core.config import settings

# Creating logs folder
os.makedirs(settings.LOG_DIR, exist_ok=True)


def setup_logger(api_version: str):
    # Setting log format
    log_format = (
        "%(asctime)s - API %(api_version)s - [%(module)s - %(levelname)s] - "
        "(%(filename)s:%(funcName)s:%(lineno)d) - %(message)s"
    )

    logname = f"api_{api_version}_{datetime.now().strftime('%Y-%m-%d')}.log"

    # Setting log filename
    log_filename = os.path.join(settings.LOG_DIR, logname)

    # Configuring logger
    logger = logging.getLogger(f"api_{api_version}")
    logger.setLevel(logging.DEBUG)

    if not logger.hasHandlers():
        # Handler for writing to file
        file_handler = logging.FileHandler(log_filename)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(log_format))

        # Handler for printing to console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter(log_format))

        # Adding handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    # Add custom context to include version
    logger = logging.LoggerAdapter(logger, {"api_version": api_version})
    return logger
