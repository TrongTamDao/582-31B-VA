from book import Book

b1 = Book("Harry Potter and Philosopher's stone", "J. K. Rowling", True)
b2 = Book("Justice, what's the right thing to do?", "Micheal J.Sandel",  True)

b1.display_info()
b2.display_info()

Book.change_library_name("West wing")
print(Book.library_name)
print(Book.is_valid_title(b1.title))