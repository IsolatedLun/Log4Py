from log4Py import Logger

import __main__
logger = Logger(__main__)

@logger.watch
def x(a, b, c=3):
    return a + b

x(10, 90, c=9)

res = x(1, 2) # ...] [{ NOW } | INFO] Executed func <add(1, 2)> fr, returned 3 ]...

if res == 3:
    logger.debug('Wow, 2 + 1 = 3!')