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
        
phone1 = Phone("Nokia",3310,2000)
phone2 = Smartphone("Realme","5s",10000,64,"8gb","48px")

print(phone1.brand)
print(phone2.ram)
print(phone2.full_name())
print(f"Phone is {phone1.brand} and the price is {phone1.price}")