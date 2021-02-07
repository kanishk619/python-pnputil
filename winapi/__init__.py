"""
The purpose of this module is to aid Windows driver enumeration
"""

__author__ = 'Kanishk Gandharv'
__version__ = '0.0.1a'
__maintainer__ = __author__
__status__ = 'alpha'

import logging


def setup_logger(name, fh=False):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)

    # formatter = logging.Formatter('[%(asctime)s,%(msecs)03d][%(levelname)-5s][%(name)-12s] - %(message)s',
    #                               datefmt="%d-%m-%Y %I:%M:%S")
    formatter = logging.Formatter('[%(asctime)s,%(lineno)03d][%(levelname)-5s][%(name)-8s] - %(message)s',
                                  datefmt="%d-%m-%Y %I:%M:%S")

    sh.setFormatter(formatter)
    logger.addHandler(sh)
    if fh:
        from logging.handlers import RotatingFileHandler
        fh = RotatingFileHandler('{}.log'.format(name), maxBytes=5242880, backupCount=10)
        fh.setLevel(logging.DEBUG)

        fh.setFormatter(formatter)
        logger.addHandler(fh)


setup_logger('winapi')  # register a root logger
