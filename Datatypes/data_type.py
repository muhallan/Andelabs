"""A function that takes one argument and compares and returns a result based on the argument supplied"""

def data_type(arg):
    """"arg is the argument whose type is to be tested"""
    if isinstance(arg, str):
        return len(arg)
    elif isinstance(arg, bool):
        return arg
    elif isinstance(arg, list):
        return arg[2] if len(arg) >= 3 else None
    elif isinstance(arg, int):
        if arg == 100:
            return "equal to 100"
        else:
            if arg < 100:
                return "less than 100"
            else:
               return "greater than 100"
    else:
        return "no value"
