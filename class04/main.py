# Class attributes vs instance attributes

class Student:
    school_name = "Vanier College" #this is our shared class attribute
    
    def __init__(self, name, program):
        #these are instance attributes / per-object state
        self.name = name
        self.program = program
        
student1 = Student("Alice", "Web Development")
student2 = Student("Karim", "Computer Science")

print(student1.name)
print(student2.name)

print(student1.school_name)
print(student2.school_name)

Student.school_name = "ABC College"
print("---------------")
print(student1.school_name)
print(student2.school_name)

# what if all students were from the same school

# the idea is:
#         some data belong to each object individually
#         Other data belong to the whole class
# 
# instance attribute => per object
# class attribute => per class - shared class-level state

#visual comparison
    # Instance attributes:
    #     create with self
    #     usually set in __init
    #     different per object
    
    # Class attributes:
    #     defined in class body
    #     shared across all instances
    #     used for common data or class-level configuration
    
class Product:
    category = "Electronics" # shared
    
    def __init__(self, name, price):
        self.name = name # per object
        self.price = price # per object
        
product1 = Product("Keyboard", 10)
product2 = Product("Mouse", 25)

print("-----------------------")

# shadowing a class attribute

class Employee:
    bonus = 0.25
    
    def __init__(self, name):
        self.name = name


employee1 = Employee("Tam")
employee2 = Employee("John")    

print(employee1.bonus) # 0.25
print(employee2.bonus) # 0.25   
print("-----------------------")

Employee.bonus = 1 # change the class attribute for all instances

print(f"Employee 1 Bonus: {employee1.bonus}") # 1
print(f"Employee 2 Bonus: {employee2.bonus}") # 1
print("-----------------------")

employee1.bonus = 2 # shadowing the class attribute for employee1   

print(f"Employee 1 Bonus: {employee1.bonus}") # 1
print(f"Employee 2 Bonus: {employee2.bonus}") # 1
print("-----------------------")

# the proccess above is shadowing, we are creating a new instance attribute called bonus for employee1, which shadows the class attribute bonus for that instance only.

Employee.bonus = 0.5

print(f"Employee 1 Bonus: {employee1.bonus}") # 1
print(f"Employee 2 Bonus: {employee2.bonus}") # 1
print("-----------------------")

# when we change the class attribute bonus to 0.5, it does not affect employee1 because it has its own instance attribute bonus that shadows the class attribute. However, it does affect employee2 because it does not have its own instance attribute bonus, so it uses the class attribute bonus which is now 0.5.

# case study:

# A good use case for class attributes is: 
    # when we have data that is shared across all instances of a class, such as a company name for employees, or a school name for students. This allows us to easily update the shared data in one place, and all instances will reflect the change.
    # conceptually the same for whole class
    # they are usually configuration-like or constant-like
    # they are counters or class-wide metadata
    
# Bad use cases for for class attributes:
    # values that should be usually be different per object, such as an employee's salary or a student's grade. Using class attributes for such data can lead to unintended consequences, as changing the class attribute will affect all instances that rely on it, which may not be the desired behavior.
    # any value that changes ofter, or is individual per object, should not be a class attribute. It can lead to bugs and confusion when multiple instances are affected by a change that was meant for only one instance.
    