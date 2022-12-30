# print the squares of numbers from 1 to 10 using list comprehensions.

squares = [i**2 for i in range(1,11)]
print(squares)

# print the negative of numbers from 1 to 10 using list comprehensions.

negative = [-n for n in range(1,11)]
print(negative)

names = ['Rohit','Virat','Dhoni','Sachin']
first_letter = [x[0] for x in names]
print(first_letter)