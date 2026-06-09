class InvalidId(Exception):
    pass

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self.__name = value
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        if not value.strip():
            raise ValueError("Email cannot be empty")
        self.__email = value
      
    def display_info(self):
        print(f"User info: \nName: {self.name} \nEmail: {self.email}")  
        
class Customer(User):
    def __init__(self, name, email, customer_id):
        super().__init__(name, email)
        self.customer_id = customer_id
        
    @property
    def customer_id(self):
        return self.__customer_id
    
    @customer_id.setter
    def customer_id(self,value):
        if not isinstance(value,str):
            raise TypeError("Customer ID must be a string")
        if not value.strip():
            raise InvalidId("Customer ID could not be empty")
        self.__customer_id = value
    
    def display_info(self):
        super().display_info()
        print(f"Customer ID: {self.customer_id}")
        
class Employee(User):
    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.employee_id = employee_id
        
    @property
    def employee_id(self):
        return self.__employee_id
    
    @employee_id.setter
    def employee_id(self,value):
        if not isinstance(value,str):
            raise TypeError("Employee ID must be a string")
        if not value.strip():
            raise InvalidId("Employee ID could not be empty")
        self.__employee_id = value
    
    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")      
             
    
    