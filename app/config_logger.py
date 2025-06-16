import logging
from logging.handlers import RotatingFileHandler
import os

from logging import Logger


def setup_logger(name) -> Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    os.makedirs('logs', exist_ok=True)

    log_file = os.path.join('logs', f'{name.replace(".", "_")}.log')

    handler = RotatingFileHandler(
        log_file,
        maxBytes=1024 * 1024,  # 1 MB
        backupCount=5,
        encoding='utf-8'
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s, line %(lineno)d - %(message)s"
    )
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
