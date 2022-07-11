from log4Py import Logger

import __main__
logger = Logger(__main__)

# IMPORTANT: the log data is always the 1st parameters!
def log_handler(data, *args):
    print('Handling received log data...')
    print((args[0] + '\n') * args[1])

# Override default save function
logger.set_log_saver(target=log_handler, args=('Hello World!', 3))

@logger.watch
def x(a, b):
    return a + b

@logger.watch
def too_many_errors():
    return bool(3) + dict([])

x(90, 90)

too_many_errors()