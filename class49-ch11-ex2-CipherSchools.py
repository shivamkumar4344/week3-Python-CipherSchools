def func(l,**kwargs):
    if kwargs.get('reverse_string') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]

names =["harshit","rohit"]
print(func(names,reverse_string = True))

