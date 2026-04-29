# write a class of employee

# class attribute is bonus =0.25

# install attributes:
#     name 
#     sales_counts    

# write a method that calculates their salary and return it 
# condition: if sales over 10 --> give bonus multiplier per sales
# Base salary is 500

class Employee:
    bonus = 0.25
    base_salary = 500
    company_name = "ABC trading"
    
    def __init__(self, name, sales_count):
        self.name = name
        self.sales_count = sales_count
        
    def calSalary(self):
        if self.sales_count > 10:
            return self.base_salary + self.sales_count * self.bonus
        return self.base_salary
    

employee1 = Employee("Tam", 11)
employee2 = Employee("John", 9)
print(employee1.company_name)
print(employee1.name)
print(employee1.calSalary())
print(employee2.name)
print(employee2.calSalary())   
