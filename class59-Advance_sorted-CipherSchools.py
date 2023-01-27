# In list form
fruits = ['mango','grapes','apple']
fruits.sort()
print(fruits)

# In tuples form
fruits2 = ('mango','grapes','apple')
print(sorted(fruits2))

# In sets form
fruits3 ={'mango','grapes','apple'}
print(sorted(fruits3))


bikes = [
    {'model':'YamahaR15','price':250000},
    {'model':'Ninja','price':700000},
    {'model':'Splendor','price':70000},
    {'model':'Duke390','price':300000}
]

# Asceding order
print(sorted(bikes , key= lambda d : d['price'])) 

# Descending order
print(sorted(bikes , key= lambda d : d['price'] , reverse=True))
