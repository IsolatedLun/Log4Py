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

### Type sheet
`

    data: {
        # Included in all
        'log_message': string,
        'log_level': string,
        'datetime': string(datetime),

        # Included in functions
        'func_name': string,
        'returned': any,
        'exc': Exception | None,
        'args': tuple,
        'kwargs': dict,
    }

`
#### Help
- Look in `examples.py` to see what the `data` dict is used for.
To put it simply, it's the 1st argument of your custom log saving function that contains all of the log info.

##### Built-in Log types
- Log (Gives the ability to insert any log type) eg. `logger.log("Hello World", "SYSTEM_FAIL")`
- Debug
- Alter
- Warn
- Error