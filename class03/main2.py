class User:
    def __init__(self, username, email = "N/A"):
        self.username = username
        self.email = email
        
user1 = User("abc", "abc@canada.ca")
user2 = User("ddd") # no email for this user

print(user1.email)
print(user2.email)

#condition inside of a method

class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    
    def sell_one(self):
       if self.stock>0: 
           self.stock = self.stock -1
           print(f"sold 1! now we have {self.stock} more left")
       else:
           print(f" {self.stock} out of stock")
        
product1 = Product("Mouse",2)

product1.sell_one()
product1.sell_one()