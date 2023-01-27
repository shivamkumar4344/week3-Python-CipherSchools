class Person:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        
    def full_name(self):
        return f"{self. first} {self.last}"
    
    def is_above_18(self):
        return self.age>18
        
p1 = Person("Shivam","Yadav",19)
p2 = Person("Bhaskar","Kumar",16)

print(p1.age)

print(p1.is_above_18())

print(p2.full_name())
print(p2.is_above_18())