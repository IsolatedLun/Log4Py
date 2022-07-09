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
        return prettify_trace(trace), f'<{type(e).__name__} than {str(e)[0:24]}..., line {trace[-1]["line"]} from origin: {trace[-1]["file"]}>'
    else:
        res += f' from "{curr_file.__file__}"'
    return res, res

def get_path_file_name(path: str):
    return path.split('\\')[-1]