# decorators - enchance the functionality of other functions.
# @ - used for decorators 

def decorator_func(anyfunction):
    def wrapper_func():
        print("This is awesome function.")
        anyfunction()
    return wrapper_func

@decorator_func
def func1():
    print("This is function 1")
    
func1()


@decorator_func
def func2():
    print("This is function 2")

func2()
    