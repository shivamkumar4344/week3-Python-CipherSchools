def to_power(x):
    def to_calc(n):
        return n**x
    return to_calc

cube = to_power(3)# to print the cube
print(cube(5))

square = to_power(2)# to print the square
print(square(8))