class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    # the type of this function/method is VOID (return nothing)  
    def desc(self):
        print(f"{self.name} is ${self.price}")
    
    # this is a return function
    def get_name(self):
        return self.name
    
    def discounted_price(self):
        new_price = self.price - 5
        return new_price
        
        
product1 = Product("Keyboard", 49.99)

print(product1.name)

#if we want the product to describe itself, change price, check availability, et.
# we should use method
product1.desc()
getName = product1.get_name()
print(f"I want to buy a new {getName}")

product1_new_price = product1.discounted_price()
print(f"You're lucky. The new price is {product1_new_price}")

# a method is a function defined inside a class that represents behaviour belonging to an object

# attribute = what an object HAS
# method = what an object DOES


# what is the difference between these two?
print(product1.name) #taking the raw data from our instance
print(product1.get_name()) #we are accessing a defined behaviour by the object

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role
        
    def show_role(self):
        print(f"{self.username} has role: {self.role}")
        
        
user1 = User("nina", "admin")
user2 = User("leo", "student")

user1.show_role()
user2.show_role()

