class Laptop:
    def __init__(self,brand_name,model_name,price):
        # instance variables
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name + ' ' + model_name
        
l1 = Laptop("Lenovo","Ideapad gaming-3",50000)
l2 = Laptop("HP","Pavilion",54000)
l3 = Laptop("Apple","Macbook Pro",130000)

print(l1.brand_name)
print(l2.model_name)
print(l3.price)
print(l3.model_name)

print(l1.laptop_name)