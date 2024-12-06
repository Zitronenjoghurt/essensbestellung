import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler

from app.constants.paths import LOGS_PATH

BLUE = '\033[94m'
CYAN = '\033[96m'
GREY = '\033[90m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'

class FileFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: f"%(asctime)s %(levelname)s    %(message)s",
        logging.INFO: f"%(asctime)s %(levelname)s     %(message)s",
        logging.WARNING: f"%(asctime)s %(levelname)s  %(message)s",
        logging.ERROR: f"%(asctime)s %(levelname)s    %(message)s",
        logging.CRITICAL: f"%(asctime)s %(levelname)s %(message)s"
    }

    def format(self, record):
        log_format = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format, "%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

class ColoredFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: f"{CYAN}{BOLD}%(levelname)s{ENDC}     %(message)s",
        logging.INFO: f"{BLUE}{BOLD}%(levelname)s{ENDC}      {BLUE}%(message)s{ENDC}",
        logging.WARNING: f"{YELLOW}{BOLD}%(levelname)s{ENDC}   {YELLOW}%(message)s{ENDC}",
        logging.ERROR: f"{RED}{BOLD}%(levelname)s{ENDC}     {RED}%(message)s{ENDC}",
        logging.CRITICAL: f"{RED}{BOLD}%(levelname)s  %(message)s{ENDC}"
    }

    def format(self, record):
        log_format = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_format)
        return formatter.format(record)

class Logger:
    def __init__(self):
        self.logger = logging.getLogger("app")
        self.logger.setLevel(logging.DEBUG)

        LOGS_PATH.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d")
        log_file = LOGS_PATH / f"{timestamp}.log"

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=10 * 1024 * 1024,
            backupCount=10
        )
        stream_handler = logging.StreamHandler()

        file_handler.setFormatter(FileFormatter())
        stream_handler.setFormatter(ColoredFormatter())

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def debug(self, message: str, **kwargs) -> None:
        self.logger.debug(message, extra=kwargs)

    def info(self, message: str, **kwargs) -> None:
        self.logger.info(message, extra=kwargs)

    def warn(self, message: str, **kwargs) -> None:
        self.logger.warning(message, extra=kwargs)

    def error(self, message: str, **kwargs) -> None:
        self.logger.error(message, extra=kwargs)

    def critical(self, message: str, **kwargs) -> None:
        self.logger.critical(message, extra=kwargs)

LOGGER = Logger()