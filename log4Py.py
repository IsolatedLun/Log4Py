from log4PyConfig import LoggerConfig
from utils import (create_log_dict, prop_or_default, prettify_params, 
    show_res_or_err, 
    get_path_file_name)
    
from datetime import datetime
from colorama import Fore, init as coloroma_int

coloroma_int()

class Logger(object):
    def __init__(self, main, config=None, log_path=None):
        self.main = main 
        self.config = prop_or_default(config, LoggerConfig)()

        self.run_checks()

        self.log_path = self.config.log_path
        self.color_codes = self.config.color_codes
    def watch(self, func):
        """
            Decorator function used for watching/logging functions.
        """
        def watch_wrapper(*args, **kwargs):
            result = None
            to_log = None
            err = None

            try:
                result = to_log = func(*args, **kwargs)
            except Exception as e:
                to_log = show_res_or_err(result, e, self.main)
                err = e

            msg = f'Executed func <{func.__name__}({readify_params(*args, **kwargs)})>, returned {to_log}'
            if err: 
                self.error(msg, create_log_dict(func.__name__, args, kwargs, e))
            else: 
                self.debug(msg, create_log_dict(func.__name__, args, kwargs))
            
            return result

        return watch_wrapper

    # ======================
    # Log functions
    # ======================
    def log(self, to_log, type, obj=None):
        """
            Typical log function.
            Displays log data and adds it somewhere depending on the config
        """

        def create_log(time, data):
            return f'[{log_time}]: {to_log} \n'

        log_time = str(datetime.now())
        to_log = create_log(log_time, to_log) 

        # Used for writing to files/databases...
        if obj:
            obj['log_time'] = log_time

            self.config.write_func(obj)
        print(to_log)

    # ======================
    # Init functions
    # ======================
    def run_checks(self):
        if getattr(self.main, '__name__', None) is None:
            raise ValueError('__main__ argument is invalid.')
    
    # =================
    # Log functions
    # =================
    def debug(self, msg: str, obj=None): return self.log(msg, 'INFO', obj)
    def warn(self, msg: str, obj=None): return self.log(msg, 'WARN', obj)
    def error(self, msg: str, obj=None): return self.log(msg, 'ERR', obj)