from status import CourseStatus

class Course:
    
    MAX_CAPACITY = 60
    
    def __init__(self, title, capacity, status):       
        
        self.title = title
        self.capacity = capacity
        self.status = status
        
        
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        if not isinstance(value, CourseStatus):
            raise ValueError("status must be CourseStatus value")
                             
        self.__status = value
    
    @property    
    def capacity(self):
        return self.__capacity
        
    @capacity.setter
    def capacity(self, value):  
        if 0< value <= Course.MAX_CAPACITY:
            self.__capacity = value
        else: 
            raise ValueError("Capacity must be greater than 0 and smaller than maximum capacity value")
        
    def display_info(self):
        print(f"{self.title}, Capacity: {self.capacity}, Status: {self.status.value}")
    
    def close_registration(self):
        self.status = CourseStatus.CLOSED
        
    def cancel_course(self):
        self.status = CourseStatus.CANCELLED
        
    def reopen_course(self):
        if self.status == CourseStatus.CLOSED:
            self.status == CourseStatus.OPEN
            print(f"Course is reopened")
        if self.status == CourseStatus.CANCELLED:
            print("a cancelled course cannot be reopened directly")
        if self.status == CourseStatus.OPEN:
            print("Course is already opened")
            
    def is_open_for_registration(self):
        return self.status == CourseStatus.OPEN