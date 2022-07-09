from const import LOGGING_COLOR_CODES
from utils import logger_default_write, prop_or_default


class LoggerConfig(object):
    def __init__(self, color_codes=None, write_func=None):
        self.color_codes = prop_or_default(color_codes, LOGGING_COLOR_CODES)

        # Where/how the log data should be stored.
        self.write_func = prop_or_default(write_func, logger_default_write)