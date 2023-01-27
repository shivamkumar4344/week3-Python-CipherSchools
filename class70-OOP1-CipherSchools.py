class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
person1 = Person("Shivam","Yadav",19)
person2 = Person("Kunal","Singh",20)
person3 = Person("Raman","Mehta",26)

print(person1.age)
print(person1.first_name)
print(person2.first_name)
print(person3.last_name)