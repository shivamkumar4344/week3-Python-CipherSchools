from functools import wraps

def only_int_allow(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        data_types = []
        if all([type(arg)== int for arg in args]):
            return function(*args,**kwargs)
        
        print("Invalid Arguments")
    return wrapper

@only_int_allow
def sum_all(*args):
    total = 0 
    for i in args:
        total+=i
    return total

print(sum_all(1,2,3,4,5,[98,0,76,56,82]))
            
        