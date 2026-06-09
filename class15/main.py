from user import Customer
from user import Employee
from status import ShowStatus
from constant import MAX_TICKETS_PER_BOOKING
from show import MovieShow
from exception import (InvalidUser, InvalidBookingError)


# CREATE USERS

customer1 = Customer("John", "john@test.com", "c001")
staff1 = Employee("Edmond", "edmond@test.com", "s001")

# DISPLAY USER INFO FOR Polymorphism
users = [customer1, staff1]
for user in users:
    user.display_info()
print("==========================================")

# CREATE A MOVIE   
movie1 = MovieShow("Harry Porter", 100, 51, ShowStatus.OPEN)
movie1.display_info()
print("============================")
# Read-only computed property
print(movie1.remaining_seats())

# Book ticket
movie1.book_tickets(customer1, 2)

print("===================================")
# Update infor:
movie1.display_info()

# Invalid operations

# booking too many tickets
try:
    movie2 = MovieShow("Odysseus", 100, 40, ShowStatus.OPEN)
    movie2.book_tickets(customer1, 100)
except InvalidBookingError as error:
        print(error)
        
# booking a sold-out show
try:
    movie3 = MovieShow("Odysseus", 100, 100, ShowStatus.OPEN)
    movie3.book_tickets(customer1, 100)
except InvalidBookingError as error:
        print(error)

# booking a cancelled show
try:
    movie4 = MovieShow("Odysseus", 100, 100, ShowStatus.CANCELLED)
    movie4.book_tickets(customer1, 100)
except InvalidBookingError as error:
        print(error)
        
# invalid capacity
try:
    movie4 = MovieShow("Odysseus", 100, 0, ShowStatus.CANCELLED)
    movie4.book_tickets(customer1, 110)
except InvalidBookingError as error:
        print(error)