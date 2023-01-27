# _name = name convention of private name.
# __name__ = dunder/magic methods

class Laptop:
    def __init__(self,brand_name,model_name,price):
        # instance variables
        self.brand_name = brand_name
        self.model_name = model_name
        self.__price = price
        
laptop1 = Laptop("HP","Pavilion",55000)
# print(laptop1._price)
# laptop1._price = 20000
# print(laptop1._price)
print(laptop1.__dict__)

print(laptop1._Laptop__price)
laptop1._Laptop__price = 20000
print(laptop1._Laptop__price)
        
        