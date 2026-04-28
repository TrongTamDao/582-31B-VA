#method writing practice
class Book:
    def __init__(self, title, author, available = True):
        self.title = title #string
        self.author = author #string
        self.available = available #boolean
        print(f"{self.title} is ready")
    # lend a book (borrow to someone)
    def borrow(self):
        if(self.available == False):
            print(f"{self.title} is already borrowed. Sorry")
        else:
            self.available = False
            print(f"{self.title} has been borrowed")
        
    # return the book (get it back)
    def return_book(self):
        if(self.available==False):
            self.available = True
            print(f"{self.title} has been returned, thank you")
        else:
            print(f"{self.title} already returned")
            

    # show the status
    def show_status(self):
        print(f"{self.title} availability: self.available")
    
book1 = Book("Game of Thrones", "Geogre R.R. Martin")
book1.borrow()
book1.borrow()
book1.return_book()
book1.return_book()