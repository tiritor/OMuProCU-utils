


from datetime import datetime
import logging
import os


class OrchestratorLoggerFormatter(logging.Formatter):
    """
    Logger format for OMuProCU to get a prettier log. 
    """
    purple = "\x1b[35m"
    blue = "\x1b[34m"
    green = "\x1b[32m"
    black = "\x1b[30m"
    white = "\x1b[37m"
    cyan = "\x1b[36m"
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    # format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    format = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"

    FORMATS = {
        logging.DEBUG: cyan + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def init_logger(logger_name, level=logging.DEBUG, log_file=None, logs_path="./logs/"):
    """
    Initialize the logger for a component.

    Parameters:
    -----------
    logger_name : str
        Name for the created logger
    level : Enum
        default log level for the created logger
    log_file : str
        Path where the logger should save the created log. If None, no log file will be created and it will be only logged to stdout.
    """
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)
    log_file_format = "{:s}-{:s}.log"
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    if log_file is None:
        log_file = log_file_format.format(logger_name, datetime.now().strftime("%Y.%m.%d-%H%M%S"))
    if not logger.hasHandlers():
        formatter = OrchestratorLoggerFormatter()
        fileHandler = logging.FileHandler("./logs/" + log_file)
        fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.addHandler(streamHandler)
    return logger

log = init_logger("Legacy-Logger")