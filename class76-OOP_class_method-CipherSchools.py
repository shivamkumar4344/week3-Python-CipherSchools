class Person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} of instances of {cls.__name__} class."
    
person1 = Person("Shivam","Yadav",19)
person2 = Person("Kunal","Singh",20)
person3 = Person("Raman","Mehta",26)
person4 = Person("Samir","Kumar",26)

print(Person.count_instances())