
import logging
from logging.handlers import RotatingFileHandler

py_logger = logging.getLogger(__name__)
py_logger.setLevel(logging.INFO)

py_handler = RotatingFileHandler(__name__, maxBytes=1024, mode="w", backupCount=5)
py_formatter = logging.Formatter("%(asctime)s file - %(funcName)s, line - %(lineno)d %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger.addHandler(py_handler)