class Phone:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    
    def full_name(self):
        return f"{self.brand} {self.name}" 
        
class Smartphone(Phone):
    def __init__(self,brand,name,price,internal_memory,ram,camera):
        super().__init__(brand,name,price)
        self.internal_memory = internal_memory
        self.ram = ram
        self.camera = camera
        
class FlagshipPhone(Smartphone):
    def __init__(self,brand,name,price,internal_memory,ram,camera,processors):
        super().__init__(brand,name,price,internal_memory,ram,camera)
        self.processors = processors
        
        
phone1 = Phone("Nokia",3310,2000)
phone2 = FlagshipPhone("Realme","5s",10000,64,"8gb","48px","Snapdragon")

print(phone2.processors)

print(phone2.full_name())

print(isinstance(Phone,Smartphone))
print(issubclass(Phone,Smartphone))