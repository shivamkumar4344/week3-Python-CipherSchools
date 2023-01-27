numbers = [1,2,4,68,97,9,99,900,765]
evens = list(filter(lambda x:x%2==0,numbers))
print("Even numbers are,",evens)

# 2nd method

for i in evens:
    print(i)