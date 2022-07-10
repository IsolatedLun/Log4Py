from log4Py import Logger

import __main__
logger = Logger(__main__)

@logger.watch
def x(a, b):
    return a + b + ''

x(90, 90)