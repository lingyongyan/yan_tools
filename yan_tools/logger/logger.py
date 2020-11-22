# coding=utf-8
"""
Program:
Description:
Author: Lingyong Yan
Date: 2019-01-08 05:10:57
Last modified: 2019-05-20 10:21:37
Python release: 3.6
Notes:
"""
import logging


def get_logger(log_file=None, verbose=2):
    """return logger
    """
    logger = logging.getLogger()
    formatter = logging.Formatter(
        '[%(levelname)-8s%(name)s-%(asctime)-10s] %(message)s')
    if isinstance(log_file, str):
        fileHandler = logging.FileHandler(log_file, 'w')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    consoleHandler.setLevel(logging.DEBUG)
    logger.addHandler(consoleHandler)

    if verbose >= 2:
        logger.setLevel(logging.DEBUG)
    elif verbose >= 1:
        logger.setLevel(logging.INFO)
    else:
        logger.setLevel(logging.WARNING)
    return logger
