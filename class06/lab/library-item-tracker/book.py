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
            
        
        
b1 = Book("Harry Potter and Philosopher's stone", "J. K. Rowling", True)
b2 = Book("Justice, what's the right thing to do?", "Micheal J.Sandel",  True)

# b1.display_book()
# b2.display_book()

print("-----------------------------------")
b1.borrow()
b1.borrow()
b1.return_book()
b1.return_book()