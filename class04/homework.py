# Exercise 1
# Implement a Book class.

# You should have a counter attribute that keeps track of how many books have been instanciated in your program.
class Book:
    counter = 0

    def __init__(self, title, author, available = True ):
        self.title = title
        self.author = author
        self.available = available
        Book.counter +=1

    def borrow(self):
        if(self.available == False):
            print(f"{self.title} is already borrowed")
        else:
            self.available = False
            print (f"{self.title} has been borrowed successfully")
            
    def return_book(self):
        if(self.available == False):
            self.available = True
            print(f"{self.title} is returned. Thank you")
        else:
            print(f"{self.title} already returned")
            
            
# Exercise 2
# Create a class called Student.

# The class should have the following class attributes:

# school_name = "Vanier College"
# student_count = 0
# Each student object should have the following instance attributes:

# name
# program
# grade
# Every time a new Student object is created, student_count should increase by 1.

# Add a method called display_info() that prints something like:

# Alice studies Web Development at Vanier College. Grade: 88
# Create at least three students and call display_info() for each one.

class Student:
    student_count = 0
    school_name = "Vanier College"
    
    def __init__(self, name, program, grade):
        self.name = name
        self.program = program
        self.grade = grade
        Student.student_count += 1  # fix here
        
    def display_info(self):
        print(f"{self.name} studies {self.program} at {self.school_name}. Grade {self.grade}") 
        

s1 = Student("Alice", "Web Development", 88)
s1.school_name = "Dawson"
s2 = Student("John", "Fullstack Development", 90)
s3 = Student("Jenifer", "Health Science", 80)

s1.display_info()
s2.display_info()
s3.display_info()
print(s2.student_count)

print("---------------------------------")
# Exercise 3
# Create a class called Product.
# It should have these class attributes:

# category = "Electronics"
# tax_rate = 0.15
# Each product should have these instance attributes:

# name
# price

class Product:
    category = "Electronics"
    tax_rate = 0.15
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Add a method called price_with_tax() that returns the price after tax.
    # Formula: price + (price * tax_rate)

    def price_with_tax(self):
        self.total_price = self.price + (self.price * self.tax_rate)
        print(f"{self.name} has price included tax: {self.total_price} ")
    

p1 = Product("Laptop", 1500)
p2 = Product("Destop screen", 400)
p3 = Product("Charging dock", 300)

# Create at least three products and print their prices with tax.

p1.price_with_tax()
p2.price_with_tax()
p3.price_with_tax()
print("------------------------------------")
# Then change the class attribute:

# Product.tax_rate = 0.20
# Print the prices with tax again.

Product.tax_rate = 0.2
p1.price_with_tax()
p2.price_with_tax()
p3.price_with_tax()
print("------------------------------------")

# Exercise 4
# Create a class called Employee.

# The class should have:

# company_name = "TechNova"
# bonus_rate = 0.10
# employee_count = 0
# Each employee should have:

# name
# salary
# Every time an employee is created, employee_count should increase by 1.



class Employee:
    company_name = "TechNova"
    bonus_rate = 0.10
    employee_count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
        
# Add a method called calculate_bonus().

# It should return:

# salary * bonus_rate

    def calculate_bonus(self):
        return self.salary * self.bonus_rate
        
# Add another method called display_employee() that prints:

# John works at TechNova. Salary: 50000. Bonus: 5000.0

    def display_employee(self):
        print(f"{self.name} works at {Employee.company_name}. Salary: {self.salary}. Bonus: {self.calculate_bonus()}")
        
# Create three employees.

e1 = Employee("John", 5000)
e2 = Employee("Jenifer", 4400)
e3 = Employee("Edmond", 6000)

# Then:

# Display all employees.
print(f"bonus rate = 0.1")
e1.display_employee()
e2.display_employee()
e3.display_employee()
print("------------------------------------")


# Change Employee.bonus_rate to 0.20.
Employee.bonus_rate = 0.2
print(f"bonus rate = 0.2")

# Display all employees again.
e1.display_employee()
e2.display_employee()
e3.display_employee()
print("------------------------------------")

# Give only one employee a custom bonus rate:

# employee1.bonus_rate = 0.50

e1.bonus_rate = 0.5
print(e1.bonus_rate)

print(f"bonus rate = 0.5 for e1")
# Display all employees again.
e1.display_employee()
e2.display_employee()
e3.display_employee()
print("------------------------------------")

# Change Employee.bonus_rate to 0.05.
Employee.bonus_rate = 0.05

# Display all employees again.
print(f"bonus rate = 0.05")
e1.display_employee()
e2.display_employee()
e3.display_employee()
print("------------------------------------")

# At the end, write a comment explaining which employee has a shadowed bonus_rate
#e1 has shadowed bonus_rate 