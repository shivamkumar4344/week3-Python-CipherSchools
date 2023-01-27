class Laptop:
    def __init__(self,brand_name,model_name,price):
        # instance variables
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name + ' ' + model_name
    
    def discount_off(self,n):
        return self.price - (n * self.price)/100
    
l1 = Laptop("Lenovo","Ideapad gaming-3",50000)
l2 = Laptop("HP","Pavilion",54000)
l3 = Laptop("Apple","Macbook Pro",130000)

print("New Price after discount is",l1.discount_off(10))