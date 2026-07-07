from user import (Customer, Employee)
# from user import Employee
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
print(movie1.remaining_seats)

# Book ticket
movie1.book_tickets(customer1, 2)

print("===================================")
# Update infor:
movie1.display_info()

print("===================================")
# Invalid operations

# booking too many tickets
try:
    movie2 = MovieShow("Odysseus", 100, 40, ShowStatus.OPEN)
    movie2.book_tickets(customer1, 130)
except InvalidBookingError as error:
        print(error)
print("===================================")        
# booking a sold-out show
try:
    movie3 = MovieShow("Odysseus", 100, 100, ShowStatus.SOLD_OUT)
    movie3.book_tickets(customer1, 100)
except InvalidBookingError as error:
        print(error)
print("===================================")
# booking a cancelled show
try:
    movie4 = MovieShow("Odysseus", 100, 100, ShowStatus.CANCELLED)
    movie4.book_tickets(customer1, 100)
except InvalidBookingError as error:
        print(error)

print("===================================")      
# invalid capacity
try:
    movie4 = MovieShow("Odysseus", -100, 0, ShowStatus.OPEN)
    # movie4.book_tickets(customer1, 110)
except ValueError as error:
        print(error)
        
# invalid user

try:
    movie1.book_tickets("",100)
except InvalidUser as error:
    print(error)