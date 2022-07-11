from Log4PyConfig.log4PyConfig import LoggerConfig
from utils import (create_log_dict, prop_or_default, prettify_params, 
    show_res_or_err, 
    get_path_file_name)
    
from datetime import datetime
from colorama import Fore, init as coloroma_int

coloroma_int()

class Logger(object):
    def __init__(
            self, main, 
            config={'color_codes': None, 'log_path': None, 'save_func': None,}, 
            log_path=None
        ):
        self.run_checks(main, config)

        self.main = main 
        self.config = LoggerConfig(self.main, **config)
    
    # =============
    # Decorators
    # =============
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

            msg = f'Executed func <{func.__name__}({prettify_params(*args, **kwargs)})>, {to_log}'
            if err: 
                self.error(msg, create_log_dict(func.__name__, args, kwargs, err))
            else: 
                self.debug(msg, create_log_dict(func.__name__, args, kwargs))
            
            return result

        return watch_wrapper

    def save(self, func):
        """
            Function to save logs with a custom function.
        """

        def save_wrapper(*args, **kwargs):
            return func(*args, *kwargs)
        return save_wrapper

    # ======================
    # Log functions
    # ======================
    def __log(self, to_log, _type, obj=None):
        """
            Typical log function.
            Displays log data and adds it somewhere depending on the config
        """

        log_time = str(datetime.now())
        to_log = self.config.format.format(time=log_time, msg=to_log, type=self.config.color_codes[_type])

        if self.config.save_func:
            self.config.save_func(obj)

        print(to_log)

    # ======================
    # Init functions
    # ======================
    def run_checks(self, main, config):
        if getattr(main, '__name__', None) is None:
            raise ValueError('No "__main__" module found.')

        if type(config) != dict:
            raise ValueError(f'Config must be a {dict}, not "{type(config)}".')
    
    # =================
    # Log functions
    # =================
    def debug(self, msg: str, obj=None): return self.__log(msg, 'INFO', obj)
    def warn(self, msg: str, obj=None): return self.__log(msg, 'WARN', obj)
    def error(self, msg: str, obj=None): return self.__log(msg, 'ERR', obj)