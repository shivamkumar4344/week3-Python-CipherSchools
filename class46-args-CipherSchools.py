# Make use of args functions as it takes the total number.. 

def all_total(*args):
    total = 0
    for i in args:
        total+=i
    return total
print(all_total(1,2,3,4,5))

# Multiplying as many numbers as you want

def multiply_num(*args):
    multiply = 1
    for i in args:
        multiply*=i
    return multiply
print(multiply_num(1,2,3,4,5))

# 2nd method if list is given

def multiply_num(*args):
    multiply = 1
    for i in args:
        multiply*=i
    return multiply

nums = [2,3,4,5,6]
print(multiply_num(*nums))  # * unpack all the packed items..




