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

    res = add(1, 2) # ...] [{ NOW } | INFO] Executed func <add(1, 2)> fr, returned 3 ]...

    if res == 3:
        logger.log(override='Wow, 2 + 1 = 3!', type='INFO')

`