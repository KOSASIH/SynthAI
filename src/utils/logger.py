import logging

def setup_logger(logger_name: str, log_file: str, level: int = logging.INFO):
    """
    Set up a logger with the specified name, log file, and log level.

    Args:
        logger_name (str): The name of the logger.
        log_file (str): The path to the log file.
        level (int): The log level (default is logging.INFO).
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # create a file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # create a formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # add the file handler to the logger
    logger.addHandler(file_handler)

    return logger
