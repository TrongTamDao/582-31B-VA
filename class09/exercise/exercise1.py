# Ex.1

# Create a class with:
#   name
#   private __gpa
# Requirements:
#   property gpa
#   setter only accepts values between 0.0 and 4.0
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.__gpa = gpa
        
    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        if(0<= value <= 4.0):
            self.__gpa = value
        else:
            print("Invalid GPA")
    
# student1 = Student("Tam",5)
# student1.gpa = 5
# print(student1.gpa)
        
# Ex.2

# Create a class with:
#   name
#   internal _price
# Requirements:
#   property price

# setter must reject negative values
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if (value>=0):
            self.__price = value
        else:
            print("Invalid price")
            
# p1 = Product("mouse", 25)
# print("====================")
# p1.price = 35
# print(p1.price)

# Ex.3 

# Create a class with:
#   radius

# Requirements:
# a read-only property area

# You should not store area directly; you should compute it.
class Round:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return 3.14*self.radius**2
    
# r1 = Round(2)
# print(r1.area)

# Ex.4 

# Create a class with:
#   first_name
#   last_name
# Requirements:
#   read-only property full_name
class User:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    @property
    def fullName(self):
        return self.firstName + " " + self.lastName
    
# p1 = User("tam","dao")
# print(p1.fullName)

# Ex.5

# Create a class with:
#   owner
#   private __balance
# Requirements:
#   property balance
#   setter prevents negative values
#   method deposit(amount)
#   method withdraw(amount)
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
    
#     @property
#     def balance(self):
#         return self.__balance
    
#     @balance.setter
#     def balance(self, value):
#         if(value>=0):
#             self.__balance = value
            
#     def deposit(self, amount):
#         if(amount > 0):
#             self.balance = amount + self.__balance
#             return self.__balance
#         else:
#             print("Invalid deposit amount")

#     def withdraw(self, amount):
#         if(amount>=0 and self.balance >= amount):
#             self.balance = self.__balance - amount
#             return self.balance
#         else:
#             print("Invalid withdraw amount")

# acc1= BankAccount("tam",-500)
# print(acc1.balance)
# print(acc1.deposit(-10))
# print(acc1.withdraw(10))

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # use setter validation

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            print("Invalid withdraw amount")
            
acc1 = BankAccount("Tam",500)
print(acc1.balance)
acc1.deposit(40)
print(acc1.balance)
# Ex.6

# Create a class with:
#   name
#   private __price
#   quantity
# Requirements:
#   property price
#   setter prevents negative values
#   read-only property inventory_value
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if(value>= 0):
            self.__price = value
        else:
            print("Invalid price")
            
    def inventory_value(self):
        return self.__price * 0.3

# p1 = Product("keyboard", 90)
# # p1 = Product("keyboard", -90)
# print(p1.price)

# Ex.7

# Create a class with:
#   title
#   private __rating
# Requirements:
#   property rating
#   setter only accepts values between 0 and 10

class Book:
    def __init__(self, title, rating):
        self.title = title
        self.__rating = rating
        
    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, value):
        if (0<= value <= 10):
            self.__rating = value
        else:
            print("Invalid input, rating should be between 0 and 10")
            
