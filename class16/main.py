# data classes

# data classes' main job is to store and represent data clearly

from dataclasses import dataclass

# Regular version
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.name = gpa
        
@dataclass
class Student:
    name: str
    gpa: float
    
s1 = Student("Alice", 3.8)
s2 = Student("Alice", 3.8)
print(s1);

print(s1 == s2)

# for simple data container, a data class is much cleaner and faster to write

# what does the dataclass give me??

# auto-generated __init__

# auto-generated display

# auto-generated equality function -- to compare different instances/objects

# how to have default values for dataclasses

@dataclass
class Course:
    title: str
    credit: int = 3 # define a default value
    
    #post_init:
    def __post_init__(self):
        # here we enforce that credits is of type int
        if not isinstance(self.credit, int):
            raise TypeError("credit must be an int")
        
# if you have a property with a default value, all the following properties should also have one.


course1 = Course("Advanced Programming")
course2 = Course("Phys Ed", 4)
# course2 = Course("Phys Ed", "a") # this throws an error now

print(course1)
print(course2)



# when is a regular class a good fit?

#   the class has lots of behaviour
#   the class enforces many invariants
#   the class has complex property logic
#   the class manages state changes heavily 

# when is a data class a good fit?

#   stores data
#   represents a record
#   all of this benefits from automatic functions such as __init__ , equality with comparisons, etc.

# methods inside a data class
@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def total_value(self):
        return self.price * self.quantity
    
product1 = Product("Keyboard", 49.99, 3)

print(product1.total_value()) # dataclass method is called