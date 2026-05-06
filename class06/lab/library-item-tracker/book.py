class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available
        
    def display_info(self):
        print(f"title: {self.title} - author: {self.author} - availability: {self.available}")
        
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
            print(f"{self.title} was returned")
            
        