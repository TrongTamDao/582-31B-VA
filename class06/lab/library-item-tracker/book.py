class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = True
        
    def display_book(self):
        print(f"title: {self.title} - author: {self.author} - avaibility: {self.available}")
        
b1 = Book("Harry Potter and Philosopher's stone", "J. K. Rowling", True)
b2 = Book("Justice, what's the right thing to do?", "Micheal J.Sandel",  True)

b1.display_book()
b2.display_book()