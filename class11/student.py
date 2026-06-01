from status import StudentLevel

class Student:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        
    @property
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        
        self.value = value
        
    @property
    def level(self):
        return self.__level
    
    @level.setter
    def level(self, value):
        if not isinstance(value, StudentLevel):
            raise ValueError("student level must be StudentLevel value")
        