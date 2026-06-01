class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius # we have our private property

    # this helps our class to understand that celsius is a private property and calling
    # celsius function basically allows access to the private property
    @property
    def celsius(self):
        return self.__celsius
    # write as a method, but use it like a field/attribute!

    # now we need a setter
    @celsius.setter
    def celsius(self, value):
        if value >= -273.15:
            self.__celsius = value
        else:
            print("Invalid temperature")

# print("======")
# t = Temperature(-500)
# print(t.celsius)
# # print(t.celsius)

# # t.celsius = 30
# # print(t.celsius)

# # t.celsius = -500
# # print(t.celsius)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative")

account = BankAccount("Alice", -500)
print("========")
account.balance = 300 # this is better than exposing our balance directly! because we have control over how it changes!
print(account.balance)
account.balance = -300