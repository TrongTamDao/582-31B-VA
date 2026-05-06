class Book:
    
    library_name = "Central Library"
    
    @staticmethod
    def is_valid_title(title):
        if(len(title.strip())>0): return True
    
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available
        
    def display_book(self):
        print(f"title: {self.title} - author: {self.author} - avaibility: {self.available}")
    
    
    @classmethod
    def change_library_name(cls, name):
        cls.library_name = name
        
