class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return Circle.pi * self.radius **2
    
    
c1 = Circle(7)
c2 = Circle(4)

print(c1.area())
print(c1.radius)
print(c2.area())