# first select only integer or floating type then convert it to string..

def num_to_str(l):
    return [str(i) for i in l if(type(i)==int or type(i) == float)]
print(num_to_str([True,"King",2,7.09,[23,44],0,'%',]))

