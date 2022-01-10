import sys
import logging
from datetime import datetime

def myConsoleHandler(level = logging.WARNING):
    # our first handler is a console handler
    console_handler = logging.StreamHandler()
    console_handler_format = '%(asctime)s | %(levelname)s: %(message)s'
    console_handler.setFormatter(logging.Formatter(console_handler_format))
    console_handler.setLevel(level)
    return console_handler

def myFileHandler(filename, level = logging.NOTSET, folder = './logs'):
    # the second handler is a file handler
    file_handler = logging.FileHandler(filename=f'{folder}/{filename}')
    file_handler_format = '%(asctime)s | %(levelname)s | %(lineno)d: %(message)s'
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter(file_handler_format))
    return file_handler


def setupLogging(logger_name, console_handler, file_handler, use_root = False):
    if use_root:
        logger = logging.getLogger()
    else:
        logger = logging.getLogger(logger_name)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info('********************STARTING A RUN***********************')
    return logger

def quickSetupLogging(logger_name):
    console_handler = myConsoleHandler()
    file_handler = myFileHandler(f'{logger_name}.log')
    return setupLogging(logger_name, console_handler, file_handler, use_root= True)