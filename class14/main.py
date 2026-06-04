# Exceptions

# raise ValueError("This is incorrect")

# number = int("hello")
# Python cannot convert hello to an integer => execution fails!
# Python raises an exeception

# So, what is an exception?
# An exception is an error signal that interrupts normal execution

# something unexpected happened
# normal execution cannot continue here **safely**

# not every problem should be handled the same way!

# IMPORTANT: Exception situations need to be handled, before they break the code!

# def set_gpa(value):
#     if value < 0 or value > 4:
#         print("Invalid GPA")

# # this would be weak:

# # it signals a problem, but does not force the caller to handle it
# # the program may continue in a bad state
# # the error is easier to ignore

# def set_gpa(value):
#     if value <0 or value >4:
#         raise ValueError("Invalid GPA")

# # now, the caller must deal with the problem or the program stops clearly
# # this is the better design

# # try, except, else, finally

# # Basic try/exceppt

# try:
#     number = int(input("enter a number: "))
#     print("You entered: ", number)
# except ValueError:
#     print("That was not a valid integer")
    
# # in this case, the may fail, and if a matching exception happens, control jumps to except

# print("end")

# # in the try/except block above, our code acknowledges if an error is happening but does not break/interrupt our runtime. This way the error is handled by the code


# try:
#     number = int(input("enter a number: "))
#     print("You entered: ", number)
# except ValueError as error: # getting the exception object
#     print("Error message: ", error)
    
# # this could also be useful to inspect or print the exception error.

# # Multiple except blocks

# try:
#     x = int(input("Enter numerator: "))
#     y = int(input("Enter numerator: "))
#     division = x/y
#     print(division)
# except ValueError:
#     print("Please enter valid integers")
# except ZeroDivisionError:
#     print("You cannot divide by zero")
    
# # else

# try:
#     number = int("42")
# except ValueError: # raise an exception, in case of an error
#     print("Conversion failed")
# else: # if it's successful, do the following
#     print("Concersion succeeded: ", number)
    
# # finally

# try:
#     print("Trying...")
#     result = 10/2
# except ZeroDivisionError:
#     print("cannot divide by zero")
# else:
#     print(f"the result is {result}")
# finally: # finally do this (regardless what happened)
#     print("Operation is over")
    
    
# Raising exception deliberately

# Programs should raise exceptions when they detect invalid situation. When that happens, we use raise

def set_age(age):
    if age<0:
        raise ValueError("Age cannot be negative")
    return age

# set_age(-5)

def withdraw(balance, amount):
    if amount>balance:
        raise ValueError("Insufficient funds")
    return balance - amount

# withdraw(1000, 1100)

# Python itself has many built-in exception types, it's up to us to use the one that matches our prob.


# Common ones that we'll use are:
# 
# ValueError
# ZeroDivisionError
# KeyError
# TypeError
# IndexError

# let's move on to exceptions in classes and invariants
# Creating a custom exception
class InvalidGPAError(Exception):
    pass

class ValidationError(Exception):
    pass

class StudenRecord:
    def __init__(self, name, gpa):
        # self.errors = []
        
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self.__name = name
        self.gpa = gpa
        
        # if self.errors:
        #   raise ValidationError("/n".join(self.errors))
        
    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        if not (0.0 < value <= 4):
            raise InvalidGPAError("GPA must be between 0.0 and 4.0")
        self.__gpa = value
        
s1 = StudenRecord("test",4)

# this is exactly where exceptions become useful in object-oriented design:

#   the class protects itself
#   invalid states are rejected clearly
#   callers must deal with the problem

# try/catching here with the class
try:
    sr2 = StudenRecord("a", 3)
except InvalidGPAError as error:
    print("Could not create student record: ", error)
except ValueError as error:
    print("Could not create student record: ", error)
except ValidationError as error:
    print(error)