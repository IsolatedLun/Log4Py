from utils import readify_params, show_res_or_err, get_path_file_name
from datetime import datetime

class Logger(object):
    def __init__(self, main, log_path=None):
        self.main = main 
        self.log_path = f'{get_path_file_name(self.main.__file__)}.log.txt' if log_path is None else log_path

    def watch(self, func):
        """
            Decorator function used for logging functions.
        """
        def watch_wrapper(*args, **kwargs):
            result = {'type': 'INFO', 'res': None}
            _e = None

            try:
                result['res'] = func(*args, **kwargs)
            except Exception as e:
                _e = e
                
                result['res'] = _e
                result['type'] = 'ERR'

            to_log, to_show = show_res_or_err(result["res"], _e, self.main)
            self.log(
                f'Executed func <{func.__name__}({readify_params(*args, **kwargs)})>, returned {to_log}', 
                f'Executed func <{func.__name__}({readify_params(*args, **kwargs)})>, returned {to_show}', 
                result['type']
            )
            return result['res']

        return watch_wrapper

    def log(self, to_log='', to_show='', type='DEF', override=None):
        """
            Prints a short version of the log to the terminal.
            Appends log to a txt file.
        """
        if override is not None:
            to_show = to_log = override

        to_log = f'[{datetime.now()} | {type}] ' + to_log + '\n' 
        to_show = f'[{datetime.now()} | {type}] ' + to_show + '\n'

        with open(self.log_path, 'w') as logf:
            logf.write(to_log)
        print(to_show)