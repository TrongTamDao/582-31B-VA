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