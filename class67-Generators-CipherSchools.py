# Getnberators are iterators..
def nums(n):
    for i in range(1,n+1):
        yield i

number = nums(10)
for no in number:
    print(no)