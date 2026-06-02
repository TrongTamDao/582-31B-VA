# 1
# Create a parent class
# Animal
# method: speak()

class Animal:
    def __init__(self, name):
        self.name = name
     
    def speak(self):
        print(f"{self.name} speak")   
# then Child class:
# Dog
# Cat
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
# Dog says "Woof"
# Cat says "Meow"
    def speak(self):
        print(f"{self.name} is a dog and speak 'Woof'")

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    
    def speak(self):
        print(f"{self.name} is a cat and speak 'Meow'")
# Then loop through them polyphorphically
animals = [Dog("Jasper"), Cat("Henry")]
for animal in animals:
    animal.speak()
print("==============")
    
#2
# Create a parent class: Vehicle
# Child class Car and Bike

# the share
# brand
# describe()
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def describe(self):
        print(f"{self.brand}, {self.model}, {self.year}")
# add child-specific behaviour

class Car(Vehicle):
    def __init__(self, brand, model, year, mileage):
        super().__init__(brand, model, year)
        self.mileage = mileage
        
    def show_mileage(self):
        super().describe()
        print(f"this car has the mileage {self.mileage}")
        
class Bike(Vehicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type
        
    def bike_type(self):
        super().describe()
        print(f"this bike is a {self.type}")
car1 = Car("Kia", "Vecolster", "2011",1000)
car1.show_mileage()
bike1= Bike("Rtype", "R", "1990", "Mountain bike")
bike1.bike_type()

# 3
# parent class: Account
#               show_type()
# children account: SavingsAccount & PremiumAccount
# override or extend behaviour accordingly

class Account:
    def __init__(self, owner, account_type):
        self.owner = owner
        self.account_type = account_type
        
    def show_type(self):
        print(f"Account type: {self.type}")

class SavingsAccount(Account):
    def __init__(self, owner, account_type, balance):
        super().__init__(owner, account_type)
        self.balance = balance
        
    def show_type(self):
        print(f"this saving account has the balance: {self.balance}")
        
class PremiumAccount(Account):
    def __init__(self, owner, account_type, interest):
        super().__init__(owner, account_type)
        self.interest = interest
        
    def show_type(self):
        print(f"this is a premium account with high interest rate: {self.interest}")
    
accounts = [
        SavingsAccount("tam","saving account", 2000), 
        PremiumAccount("ngan","premium account", 7.7)
        ]

for account in accounts:
    account.show_type()