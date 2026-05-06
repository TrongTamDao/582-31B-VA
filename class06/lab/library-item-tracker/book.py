class Book:
    
    library_name = "Central Library"
    count = 0
    
    @staticmethod
    def is_valid_title(title):
        if(len(title.strip())>0): return True
    
    def __init__(self, title, author, genre, available):
        self.title = title
        self.author = author
        self.available = available
        self.genre = self.genre
        Book.count += 1
        
    def display_info(self):
        print(f"title: {self.title}")  
        print(f"author: {self.author}")
        print(f"genre: {self.genre}")
        print(f"availability: {self.available}")
        
    def borrow(self):
        if self.available == True: 
            self.available = False
            print(f"{self.title} has been borrowed.")
        else: print(f"{self.title} is not available.")
    
    def return_book(self):
        if self.available == False:
            self.available = True
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already returned")
    
    
    @classmethod
    def change_library_name(cls, name):
        cls.library_name = name
        
    @classmethod
    def show_count(cls):
        print(f"total book: {cls.count}")
        
    @classmethod
    def from_string(cls, data):
        title, author, available = data.split(",")
        return cls(title, author, available)
        
        
