# 1
# Create a class with:
#   private balance
#   deposit(amount)
#   withdraw(amount)
# 
# Use exceptions for:
#   negative deposit
#   negative withdrawal
#   insufficient funds

class InvalidOwnerName(Exception):
    pass
class InvalidBalance(Exception):
    pass
class InvalidDeposit(Exception):
    pass
class InvalidWithdraw(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance):
        if not owner.strip():
            raise InvalidOwnerName("Name cannot be empty")
        self.__owner = owner
        self.balance = balance
        
    @property
    def owner(self):
        return self.__owner  
      
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value <0 :
            raise InvalidBalance("Balance could not be negative")
        self.__balance = value
        
    def deposit(self, amount):
        if amount < 0:
            raise InvalidDeposit("Deposit could not be negative")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount < 0:
            raise InvalidWithdraw("Withdraw could not be negative")
        if amount > self.balance:
            raise InvalidWithdraw("Insufficient funds")
        self.balance -= amount
    

try:
    acc1 = BankAccount("tam", 1000)
    print(acc1.owner)
    print (acc1.balance)
    acc1.withdraw(200)
    print(acc1.balance)
    acc1.deposit(200)
    print(acc1.balance)
except (InvalidOwnerName, InvalidBalance) as error:
    print("Could not create account: ", error)
except (InvalidDeposit, InvalidWithdraw) as error:
    print("Could not complete the transaction: ", error)
else:
    print(f"Owner name: {acc1.owner}, Current balance: {acc1.balance}")
print("======================================")

# 2
# Create a class with:
#   property celsius
# 
# 
# Raise an exception if:
#   temperature is below absolute zero
class Temp:
    def __init__(self, celsius):
        if celsius < -273:
            raise ValueError("temperature is below absolute zero")
        self.celsius = celsius
        
try:
    t1 = Temp(-274)
    print (t1.celsius)
except ValueError as e:
    print(e)
else:
    print(t1.celsius)
    
print("===========================")
    
# 3
# Create:
# class NegativePriceError(Exception):
#     pass

# Then use it in a Product class.

class NegativePriceError(Exception):
    pass

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self.__name = value
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise NegativePriceError("Price could not be negative")
        self.__price = value
        
try:
    p1 = Product("laptop", -1200)
except ValueError as e:
    print(e)
except NegativePriceError as e:
    print(e)
else:
    print(p1.name, p1.price)
finally:
    print("Operation finished.")