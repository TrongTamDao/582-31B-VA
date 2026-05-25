class CourseSection:
    def __init__(self, title, capacity, enrolled, waitlist = 0):
        self.title = title
        self.__capacity = capacity
        self.__enrolled = enrolled
        self.__waitlist = waitlist
        
    @property
    def title(self):
        return self.__title 
    
    @title.setter
    def title(self,value):
        if (value.strip()):
            self.__title = value
        else:
            raise ValueError ("Invalid title")
    
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
            raise ValueError("Invalid input: Capacity must be greater than 0")
            
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
            raise ValueError("Invalid input for enrolled")
            
    def register_student(self):
        if self.__enrolled < self.__capacity:
            self.__enrolled += 1
            print(f"Student registered successfully. Enrolled: {self.__enrolled}/{self.__capacity}")
        else:
            raise ValueError ("Maximum enrolled reached")
            
    def drop_student(self):
        if(self.enrolled > 0):
            self.__enrolled -= 1
            print(f"Student dropped successfully. Enrolled: {self.__enrolled}/{self.__capacity}")
        else:
            raise ValueError ("Minimum enrolled reached")
    
    def display_info(self):
        print(f"{self.title} with total {self.__enrolled} enrolled, capacity: {self.__capacity}")
        
    @property
    def waitlist(self):
        return self.__waitlist
    
    @waitlist.setter
    def waitlist(self, value):
        if value >= 0:
            self.__waitlist += value
        else:
            raise ValueError ("Waistlist cannot be negative")
    
    def add_to_waitlist(self):
        self.__waitlist += 1

        
    def remove_from_waitlist(self):
        if self.__waitlist > 0:
            self.__waitlist -=1
        else:
            raise ValueError ("Waitlist is at 0. Cannot remove")

# c1 = CourseSection("web design", 12, 12)
# c1.capacity = 13
# c1.display_info()
# c1.drop_student()
# print(c1.enrolled)
# print(c1.register_student())
