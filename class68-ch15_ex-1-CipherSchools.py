# Generator to  define a function for even function..

def even_gen(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
            
even_nums = even_gen(20)
for nums in even_nums:
    print(nums) 