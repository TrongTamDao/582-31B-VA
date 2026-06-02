# Inheritance


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
        if 0.0<= value <= 4:
            self.gpa = value
        else:
            raise ValueError('Invalid GPA')
        
# Invariants: it's a rule that must always remain true

from enum import Enum

class CourseStatus(Enum):
    OPEN = "open"
    CLOSE = "close"
    CANCELLED = "closed"
    
status = CourseStatus.OPEN
print(status.value)

#enume reduce invalid values and improve readability
# for example: CourseStatus class becomes a container for a series of constants

# all of the concepts above help us design one class properly

class User:
    def __init__(sefl, username):
        sefl.username = username
        
    def introduce(self):
        print(f"Hello, my name is {self.username}")
        
class StudentUser(User): #extending the User class
    def __init__(self, username, program):
        super().__init__(username) # super means go to the parent class and in here we refer to the parent class' constructor
        self.program = program
        
s1 = StudentUser("Jane", "Web Dev")
s1.introduce()
print (s1.program)

# super()__init__(name) calls parent
    # super is very important
    
# ============================

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
e1 = Employee("Jane", "Software Devep")

p1.introduce()
e1.introduce()

class Admin(Person):
    def __init__(self, name, dpt):
        super().__init__(name)
        self.dpt = dpt
        
    def introduce(self):
        super().introde() # first execute parent method
        print(f"I oversee the {self.dpt} department") # then add the overriden stuff
        
# Polymorphism: means diferent objects can respond to the same method call in their own ways

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
    def introduce(self):
        print(f"")


        