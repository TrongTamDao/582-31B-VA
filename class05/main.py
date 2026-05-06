# instance method vs class method

class Student:
    school_name = "ABC college"
    
    def __init__(self, name):
        self.name = name
    
# Sometimes, we might need a method that changes a class atribute
# We might also need a helper method that checks if everything is valid
# from here we move toward class methods and static methods
# Instance methods, take self and they work with one object

# if we go towards a class method:
    # class method works with the class itself
    # it receives cls instead of self (as signature)
    # its also marked with @classmethod
    
    @classmethod # we add the mark
    def show_school(cls): #cls as signature
        print(f"School: {cls.school_name}")  #cls instead of self
        
    # instance method
    # here introduce belongs to an instance of class Student
    
    def introduce(self):
        print(f"My name is {self.name}")
        
student1 = Student("John Doe")
student2 = Student("Jane Doe")

student1.introduce()
student2.introduce()

Student.show_school()
print("---------------------------------------")
# compare them directly:

    # instance methods:
        # first parameter: self(ALWAYS)
        # use only one object: uses only one object
        
    # Class methods:
        # first parameter: cls (ALWAYS)
        # uses the class
        
class Product:
    count = 0
    
    def __init__(self, name):
        self.name = name
        # Product.count += 1
        self.increment_count()
        
    @classmethod
    def show_count(cls):
        print(f"Total products: {cls.count}")
    
    # class method that updates a shared attribute
    @classmethod
    def increment_count(cls):
        cls.count += 1
        
p1 = Product("Keyboard")
p2 = Product("Mouse")
p3 = Product("Keyboard")
print(p1.count)
Product.show_count()
    
# let's move the design patern