class CourseSection:
    def __init__(self, title, capacity, enrolled):
        self.title = title
        self.__capacity = capacity
        self.__enrolled = enrolled
        
    @property
    def title(self):
        return self.__title 
    
    @title.setter
    def title(self,value):
        if (value.strip()):
            self.__title = value
        else:
            print("Invalid title")
    
    @property
    def capacity(self):
        return self.__capacity
    
    # Getter
    def get_capacity(self):
        return self.__capacity
    
    # Setter
    @capacity.setter
    def capacity(self, value):
        if (value > 0):
            self.__capacity = value
        else:
            print("Invalid input: Capacity must be greater than 0")
            
    @property
    def enrolled(self):
        return self.__enrolled
    
    # Getter
    def get_enrolled(self):
        return self.__enrolled
    
    # Setter
    @enrolled.setter
    def enrolled(self, value):
        if(0<value<self.__capacity):
            self.__enrolled = value
        else:
            print("Invalid input for enrolled")
            
    def register_student(self):
        if(self.__enrolled < self.__capacity):
            self.__enrolled += 1
        else:
            print("Maximium enrolled reached")
            
    def drop_student(self):
        if(self.enrolled > 0):
            self.__enrolled -= 1
        else:
            print("Minimum enrolled reached")
    
    def display_info(self):
        print(f"{self.title} with total {self.__enrolled} enrolled, capacity: {self.__capacity}")
        

c1 = CourseSection("web design", 12, 12)
c1.capacity = 13
c1.display_info()
c1.drop_student()
print(c1.enrolled)
print(c1.register_student())
