# ==============
# Log utils
# =============
def readify_params(*args, **kwargs):
    """
        Converts *, ** params to a readable string format.
    """
    res = str(args).replace('(', '').replace(')', '')

    for (key, val) in kwargs.items():
        res += f', {key}={val}'
    return res

def show_res_or_err(res: str, e: Exception, curr_file):
    """
        Shows the result or error if there is an exception.
        Exceptions are shown with all of their tracebacks.
    """
    res = str(res)

    def prettify_trace(trace):
        res = 'returned ERR'

        for x in trace:
            res += f'\n \t Error: at line {x["line"]}, in {x["file"]}'
        return res

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

def create_log_dict(f_name, args, kwargs):
    return {
        "func_name": f_name,
        "args": args,
        "kwargs": kwargs,
    }

def logger_default_write(obj):
    # WIP
    print(obj)

# ============
# Short-hands
# ============
def prop_or_default(x, default):
    return x if x is not None else default

def get_path_file_name(path: str):
    return path.split('\\')[-1]