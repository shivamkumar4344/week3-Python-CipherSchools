# define a function take any no. of lists containing number
# return average
# try by using lambda 

average_finder = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(average_finder([1,2,3],[4,5,6],[7,8,9]))