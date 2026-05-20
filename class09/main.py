# Properties

# properties let us keep simple attribute-style access while secretly adding validation 
# and control behind the scene

# a property lets an attribute look simple from the outside while being managed by methods
# inside the class.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius


t = Temperature(25)

t.celsius = 500 #this is problematic!

# with encapsulation and properties
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    # we need to define a getter function!
    def get_celsius(self):
        return self.__celsius
    
    # we also need to define a setter function!
    def set_celsius(self, value):
        if value >= -273.15:
            self.__celsius = value
        else:
            print("invalid temperature")

temp = Temperature(25)

print(temp.get_celsius())

temp.set_celsius(30)

print(temp.get_celsius())

# these work, but it feels clumsy!
#   1. users of the class must remember method names
#   2. syntax becomes less natural!
#   3. simple attribute access becomes verbose

class Temparature:
    def __init__(self, celsius):
        self.__celsius = celsius # we have our private property
        
    # this helps our class to understand that celsius is a private property and calling
    # celsius function basically allows access to the private property
    @property
    def celsius(self):
        return self.__celsius
    # write as a method, but use it like a field/attribute!

new_temp = Temparature(60)
print(new_temp.celsius)

class Temperature_Wrong:
    @property
    def celsius(self):
        return self.celsius

temp_wrong = Temperature_Wrong()

# temp_wrong.celsius # this causes a recursive problem! (as in it keeps calling itself without any breaks!)
    
# remember the property and the internal storage name must be different!

# let's try rewriting our class with a setter now!
class Temparature:
    def __init__(self, celsius):
        self.__celsius = celsius
        
    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if value <= -273.15:
            self.__celsius = value
        else:
            print(f"-500 Invalid temparature")
            
# print("==============================")
# t = Temparature(25)
# print(t.celsius)

# t.celsius = 30
# print(t.celsius)

# t.celsius = -500
# print(t.celsius)

# Another important point for properties:
# Properties let the class protect the data without changing the outside syntax!

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative")
            

account = BankAccount("Tam", -500),#still accept negative value
print("bank account========================")
account.balance = -500 ## this is better than exposing our balance directly! because we have control over how it changes!
print(account.balance)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self): # this is read only!
        return self.width * self.height
    
# what does read only mean?
# it cannot be changed under any circumstances!

print("==========")
r = Rectangle(4, 5)
print(r.area)

# r.area = 50 - this would fail, because it has no setter! the object is read-only!!!

# Stored managed property:

#   backed by private state (the class!!)
#   often has getter and setter

# Computed read-only property
#   derived from other attributes
#   may only need @property , no setters..