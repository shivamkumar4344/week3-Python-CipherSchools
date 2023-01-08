# print the squares with the dictionary comprehension.

square = {f"Square of {num} is":num**2 for num in range(1,11)}
print(square)

print("\n")

for k,v in square.items():
    print(f"{k}:{v}")
    
print('\n')  
 
# Dictionary comprehension with if and else 

odd_even = {i:('even' if i%2==0 else 'odd')for i in range(1,11)}
print(odd_even)

print("\n")

for key,value in odd_even.items():
    print(f"{key}:{value}")