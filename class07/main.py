# Interfaces / Abstraction
# so far we've built concrete classes

class Book:
    def __init_(self, name):
        self.name = name
    
    def display_info(self):
        print(f"Book name is: {self.name}")

class Product:
    def __init_(self, name, price):
        self.name = name
        self.price = price
        
    def display_info(self):
        print(f"Product name is {self.name}")
        
# let's move one level higher than just concrete classes
# instead of asking what one object does, we ask what a whole category of object should be able to do

# in the examples above, we see that our classes might behave in a similar way and we want to think of abstraction as a way that allows us to design our code

# Imagine a pyament system --> every payment method must have a pay(amount) operation
# but!! a creidt card pays one way -- PayPal pays another way -- bank transfer works differently, etc..

# the shared idea for the above: is the abstraction "a payment method can make a payment"

# abstraction allows us to have
# 1. clearer design
# 2. less duplication
# 3. easier extensino
# 4. more consistent behaviour
# 5. in case of larger code bases: better teamwork and maintainbility

# let's get practical now

# the common approach to use interfaces in python is:
# abstract base classes using the abs module

# 1. import interface module

from abc import ABC, abstractmethod

class Shape(ABC):  #ABC means this class is abstract
    @abstractmethod # we make a method that subclassess must implement
    def area(self):
        pass
    
# VERY IMPORTANT: Shape on its own cannot and must not be instantiated directly

class Rectangle(Shape): #Implement Abstract class SHAPE
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    # MUST define area(), otherwise it throws an error
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return self.radius ** 2 * 3.14
    

rectangle = Rectangle(3,4)
circle = Circle(3)

print(rectangle.area())
print(circle.area())

# this could be the code that interacts with our classes
def print_area(shape):
    print(shape.area())

print_area(rectangle)
print_area(circle)

# another example

# This is our CONTRACT
class FinancialInstitution(ABC):
    @abstractmethod
    def payment(self, amount):
        pass

class Visa(FinancialInstitution):
    def __init__(self, card_number):
        self.card_number = card_number
        self.balance = 0

    def payment(self, amount):
        self.balance += amount
        print(f"{amount} withdrawn! by Visa")

    def show_balance(self):
        print(self.balance)

class PayPal(FinancialInstitution):
    def __init__(self, card_number, debit_balance):
        self.card_number = card_number
        self.debit_balance = debit_balance

    def payment(self, amount):
        self.debit_balance -= amount
        print(f"{amount} paid by Paypal!")

    def donate(self):
        pass

visa_card = Visa("123")
paypal_account = PayPal("456", 100)

print("===========")
def checkout(amount, fi):
    print(f"You owe ${amount}")
    fi.payment(amount)

checkout(50, paypal_account)


# another example

# i want to have multiple animal classes (dog, cat, etc..)