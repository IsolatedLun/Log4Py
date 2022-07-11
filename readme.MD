# Log4Py, The Best Logger for Python. 
With 0 Vulnerabities... well hopefully.

## Usage
`

    from log4Py import Logger
    import __main__

    logger = Logger(__main__)

    @log.watch
    def add(a, b):
        return a + b

    res = add(1, 2) # Check terminal

    if res == 3:
        logger.debug('Wow, 2 + 1 = 3!')
    else:
        logger.error('What the hell')

`