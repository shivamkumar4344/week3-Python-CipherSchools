from functools import wraps
import time

def calculate_time(function):
    @wraps(function)
    def wrappers(*args,**kwargs):
        print(f"executing-->{function.__name__}")
        t1 = time.time()
        returned_value = function(*args,**kwargs)
        t2 = time.time()
        total_time = t2-t1
        print(f"This function took {total_time}")
        return returned_value
    return wrappers
    
@calculate_time
def square(n):
    return [i*i for i in range(1,n+1)]

square(10000)
        