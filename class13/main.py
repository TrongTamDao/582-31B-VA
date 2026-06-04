# Inheritance
# what happens when several classes are related and should share common behaviour without duplicating code

#but first, let's do a quick recap

# Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
# Encapsulation says: object state should be protected intentionally

#Properties:
#let use keep clean attribute syntax
#validate and/or control access to our attributes:

class Student:
    def __init__(self, gpa):
        self.gpa = gpa
        
    @property
    def gpa(self, value):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        if 0.0<= value <= 4: # this is an invariant
            self.gpa = value
        else:
            raise ValueError('Invalid GPA')
        
# Invariants: it's a rule that must always remain true
# good classes prevent invalid states

# Constans and Enum

from enum import Enum

# once value is set, you cannot change it in runtime in Python

class CourseStatus(Enum):
    OPEN = "open"
    CLOSE = "close"
    CANCELLED = "closed"
    
status = CourseStatus.OPEN
print(status.value)

#enume reduce invalid values and improve readability
# for example: CourseStatus class becomes a container for a series of constants

# all of the concepts above help us design one class properly
# Inheritance = shared structure + specialization

class User:
    def __init__(sefl, username):
        sefl.username = username
        
    def introduce(self):
        print(f"Hello, my name is {self.username}")
        
class StudentUser(User): #extending the User class
    def __init__(self, username, program):
        super().__init__(username) # super means go to the parent class and in here we refer to the parent class' constructor
        self.program = program

class AdminUser(User):
    def __init__(self, username, dpt):
        super().__init__(username)
        self.dpt = dpt

# super()__init__(name) calls parent
    # super is very important
    
s1 = StudentUser("Jane", "Web Dev")
s1.introduce()
print (s1.program)

admin1 = AdminUser("John", "Accounting")
print(admin1.introduce())

# class StudentUser(User):
#     def ___init__(self, username, program):
#         super().__init__(username)
#         print("hello from child constructor")
#         self.program = program

# class AdminUser(User):
#     def __init__(self, username, dpt):
#         super().__init__(username)
#         self.dpt = dpt
        
# s1 = StudentUser("Jane", "Web Dev")
# s1.introduce()
# print(s1.program)
    
print("============================")

# Method overriding

# a child class can replace or customize inherited behaviour --> this is called overriding

class Person:
    def __init__(self, name):
        self.name = name
        
    def introduce(self):
        print(f"hello, my name is {self.name}")
        
class Employee(Person):
    def __init__(self, name, dpt):
        super().__init__(name)
        self.dpt = dpt
        
    #we override the parent method
    
    def introduce(self):
        print(f"hello, my name is {self.name} and I work at the {self.dpt}")
        
p1 = Person("John")
e1 = Employee("Jane", "Software Dev")

p1.introduce()
e1.introduce()

class Admin(Person):
    def __init__(self, name, dpt):
        super().__init__(name)
        self.dpt = dpt
        
    def introduce(self):
        super().introduce() # first execute parent method
        print(f"I oversee the {self.dpt} department") # then add the overriden stuff
        
# Polymorphism: means diferent objects can respond to the same method call in their own ways

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
    def introduce(self):
        print(f"Hello, my name is {self.name} and I teach {self.subject}")
        
        
print("=========================")

people = [
    Person("Nadia"),
    Employee("Ahmed", "Accounting"),
    Admin("Janice", "HR"),
    Teacher("Kymuar", "Advance Programming")
]

for person in people:
    person.introduce()


        