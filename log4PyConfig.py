from const import LOGGING_COLOR_CODES
from utils import (logger_default_write, prop_or_default, get_path_file_name)


class LoggerConfig(object):
    def __init__(self, main, color_codes=None, write_func=None, log_path=None):
        self.color_codes = prop_or_default(color_codes, LOGGING_COLOR_CODES)
        self.log_path = prop_or_default(log_path, f'{get_path_file_name(self.main.__file__)}.log.txt')

        # Where/how the log data should be stored.
        self.write_func = prop_or_default(write_func, logger_default_write)