class StudentRecord:
    def __init__(self, name, gpa, credit):
        self.name = name
        self.__gpa = gpa
        self.__credit = credit
    
    # NAME
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, str):
        if (str.strip()):
            self.__name = str
        else:
            raise ValueError("Invalid name: Name cannot be empty")
    
    # GPA    
    @property
    def gpa(self):
        return self.__gpa
    
    #Getter function
    def get_gpa(self):
        return self.__gpa
    
    # Setter function
    @gpa.setter
    def gpa(self, value):
        if (0<= value <= 4):
            self.__gpa = value
        else:
            raise ValueError("Invalid value: GPA must be between 0.0 and 4.0")
    
    # CREDIT       
    @property
    def credit(self):
        return self.__credit
    
    #Getter function
    def get_credit(self):
        return self.__credit
    
    #Setter function
    @credit.setter
    def credit(self, value):
        if (value >= 0):
            self.__credit = value
        else:
            raise ValueError("Invalid credit: Credit must be greater than or equal to 0")
    
    def add_credit(self, amount):
        if (amount > 0):
            self.__credit += amount
        else:
            raise ValueError ("Invalid input value: credit must be greater than 0")
    
    def update_gpa(self, amount):
        if (0<=amount<=4):
            self.__gpa = amount 
        else:
            raise ValueError ("Invalid value: GPA must be between 0.0 and 4.0")
    
    def display_info(self):
        print(f"{self.name} has GPA: {self.__gpa} with {self.__credit} credit")
        
    @property
    def academic_status(self):
        if self.__gpa < 2:
            return "At risk"
        elif self.__gpa < 3.5:
            return "Good standing"
        else:
            return "Honours"
# class StudentRecord:
#     def __init__(self, name, gpa, credit):
#         self.name = name        # uses setter
#         self.gpa = gpa          # uses setter
#         self.credit = credit    # uses setter
        
#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, value):
#         if value.strip():   # rejects empty string or spaces only
#             self.__name = value
#         else:
#             print("Invalid name: Name cannot be empty")
        
#     @property
#     def gpa(self):
#         return self.__gpa
    
#     @gpa.setter
#     def gpa(self, value):
#         if 0 <= value <= 4:
#             self.__gpa = value
#         else:
#             print("Invalid value: GPA must be between 0.0 and 4.0")
           
#     @property
#     def credit(self):
#         return self.__credit   # fixed typo
    
#     @credit.setter
#     def credit(self, value):
#         if value >= 0:
#             self.__credit = value
#         else:
#             print("Invalid credit: Credit must be greater than or equal to 0")
            
s1 = StudentRecord("tam", 10, -4)
# s1.name = "ngan"
# # s1.credit = -9
# print(s1.name)
# print(s1.gpa)
# print(s1.credit)
# print("=================")
# s1.name = ""
# s1.gpa = 11
# s1.credit = -5
# print(s1.name)
# print(s1.gpa)
# print(s1.credit)
# s1.display_info()
# s1.add_credit(10)
# s1.display_info()
