if __name__ == '__main__':
    import __main__
    from log4Py import Logger

    logger = Logger(__main__)

    # IMPORTANT: the log data is always the 1st parameter.
    def log_handler(data, *args):
        # in_save is used to avoid recursion
        # Since log_handler is called everytime a log happens, we need to do this.
        logger.warn(f'Handling received log data... for', in_save=True)
        logger.debug((args[0] + '\n') * args[1], in_save=True)

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

    logger.set_level('FATAL', 35) # Purple color code
    logger.log('Purple log', 'FATAL')