# print even and odd numbers from the range 0 to 10.

even_nums = [i for i in range(0,11) if i%2==0]
print(even_nums)

odd_nums = [i for i in range(0,11) if i%2 !=0]
print(odd_nums)

# return *2 for even numbers and negative for odd numbers

nums = [1,2,3,4,5,6,7,8,9,10]
new_nums = [x**2 if(x%2==0) else -x for x in nums]
print(new_nums)