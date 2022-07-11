# ==============
# Prettifiers
# ==============
def prettify_params(*args, **kwargs):
    """
        Converts *, ** params to a readable string format.
    """
    res = str(args).replace('(', '').replace(')', '')

    for (key, val) in kwargs.items():
        res += f', {key}={val}'
    return res

def prettify_trace(trace):
    """
        Prettifies the traceback of an error.
    """
    res = 'returned ERR'

    for x in trace:
        res += f'\n \t Error: at line {x["line"]}, in {x["file"]}'
    return res

# ==============
# Log utils
# ==============
def show_res_or_err(res: str, e: Exception, curr_file):
    """
        Shows the result or error if there is an exception.
        Exceptions are shown with all of their tracebacks.
    """

    res = str(res)

    if e:
        trace = []
        tb = e.__traceback__

        while tb is not None:
            trace.append({
                'line': tb.tb_lineno,
                'file': tb.tb_frame.f_code.co_filename,
            })
            tb = tb.tb_next

        return prettify_trace(trace)
    else:
        res += f' from "{curr_file.__file__}"'
    return res

def create_function_log_dict(f_name: str=None, args: tuple=None, kwargs: dict=None, 
    returned=None, exc: Exception=None):
    return {
        "func_name": f_name,
        "returned": returned,
        "args": args,
        "kwargs": kwargs,
        "exception": exc,
    }

# ==============
# Log config utils
# ==============
def default_log_saver(data: dict, *args):
    from os import path, mkdir

    if path.exists(args[0]):
        with open(args[0] + '/' + args[1], 'a+') as f:
            f.write(f'[{data["datetime"]}] {data["log_message"]} _{data["type"]}_' + '\n\n')
        
        return;
    else:
        mkdir(args[0])

    return default_log_saver(data, *args)

# ==============
# Misc
# ==============
def is_function(x):
    from types import FunctionType

    return isinstance(x, FunctionType)


# ============
# Short-hands
# ============
def prop_or_default(x, default):
    return x if x is not None else default

def get_path_file_name(path: str):
    return path.split('\\')[-1]