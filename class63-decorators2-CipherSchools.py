def decorator_func(anyfunction):
    def wrapper_func(*args,**kwargs):
        print("This is awesome function.")
        return anyfunction(*args,**kwargs)
    return wrapper_func

@decorator_func
def func(a):
    print(f"The function with argument {a}.")
    
func(7)

@decorator_func
def add(a,b):
    return a+b

print(add(2,8))


