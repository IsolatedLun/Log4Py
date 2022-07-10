from Log4PyConfig.const import LOGGING_COLOR_CODES, LOGGING_FORMAT
from utils import (prop_or_default, get_path_file_name)


class LoggerConfig(object):
    def __init__(self, main, color_codes=None, save_func=None, log_path=None):
        self.main = main

        self.color_codes = prop_or_default(color_codes, LOGGING_COLOR_CODES)
        self.log_path = prop_or_default(log_path, f'{get_path_file_name(self.main.__file__)}.log.txt')
        self.format = LOGGING_FORMAT

        # Where/how the log data should be stored.
        self.write_func = prop_or_default(save_func, None)