from functools import wraps

def print_function_data(function):
    @wraps(function)
    def wrappers(*args,**kwargs):
        print(f"You are calling {function.__name__} function.")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrappers

@print_function_data
def addition(a,b):
    '''this is an addition function.. '''
    return a+b

print(addition(8,7))