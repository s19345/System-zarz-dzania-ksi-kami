import logging
import os


def set_up_logger(name: str) -> logging.Logger:
    """creates and configures a logger with file and console output.
    The logger logs errors and warnings to file or console."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    os.makedirs("logs", exist_ok=True)
    file_handler = logging.FileHandler(f"logs/app_logs.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
