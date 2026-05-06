data = "test1, test2"

print(data.split(","))

# split is a string method that converts a string into a list by common denominator
    # in case above it's a ","
    
# let's move toward our first design pattern

# alternative constructor:

class Student:
    def __init__(self, name, program): # main constructor
        self.name = name
        self.program = program

    # we keep object-creation logic inside the class
    # helping the object creation to be dynamic!
    @classmethod
    def from_string(cls, data): # alternative constructor
        name, program = data.split(",")
        return cls(name, program)
    
    @classmethod
    def from_form(cls, data):
        # parse the data according to how it's received!
        pass
    # what if we want a new object out not all the input
    
    @classmethod
    def newly_admitted(cls, name):
        return cls(name,"")
    
# student1 = Student("Alice", "Web Development") # valid!
student1 = Student.from_string("Alice,Web Development") # Alternative Constructor

print(f"{student1.name} studies in {student1.program}")

student2 = Student.newly_admitted("John")

print(f"{student2.name} studies in {student2.program}")


# in real program, data often comes in a variety of formats! 

    # for example: 
        # comma-separated strings (csv, excel sheet, etc.)
        # a dictionary
        # as a database row
        # as a JSON object
        # sometimes a user input that needs conversion

# so for example if you have in your database, or a excel sheet:
# value1,value2,value3, etc..

# using the alternative constructor we can parse the data properly!