from user import (Customer, User, Employee)
# from user import User
# from user import Employee
from status import ShowStatus
from constant import MAX_TICKETS_PER_BOOKING
from exception import (InvalidUser, InvalidBookingError)



class MovieShow:
    def __init__(self, title, capacity, book_seats, status):
        self.title = title
        self.capacity = capacity
        self.book_seats = book_seats
        self.status = status
        
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Title cannot be empty")
        self.__title = value
        
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.__capacity = value
        
    
    @property
    def book_seats(self):
        return self.__book_seats
    
    @book_seats.setter
    def book_seats(self, value):
        if 0<=value<=self.capacity:
            self.__book_seats = value
        else:
            raise ValueError("Booked seats are not valid")
        
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        if not isinstance(value, ShowStatus):
            raise TypeError("Status must be a ShowStatus")
        
        self.__status = value
    
    def remaining_seats(self):
        return self.capacity - self.book_seats
        
    def book_tickets(self, customer, quantity):
        if not isinstance(customer,(Customer, Employee)):
            raise InvalidUser("Only customer or staff can do the booking")
        
        if self.status != ShowStatus.OPEN:
            raise InvalidBookingError("Show either cancelled or sold_out")
        
        if not isinstance(quantity, int):
            raise InvalidBookingError("Booking quantity must be an integer")
        
        if not (0<= quantity <= MAX_TICKETS_PER_BOOKING):
            raise InvalidBookingError("Booking quantity must not be negative or greater than maximum booking per person")
        
        if self.book_seats + quantity > self.capacity:
            raise InvalidBookingError("Not enough available seats.")
        
        self.book_seats += quantity
        
        print(f"Booking successful. {customer.name} booked {quantity} tickets")
    
    def cancel_show(self):
        self.status = ShowStatus.CANCELLED
            
    def display_info(self):
        print(f"Show info:\n"
              f"Title: {self.title}\n"
              f"Capacity: {self.capacity}\n"
              f"Booked seats: {self.book_seats}\n"
              f"Status: {self.status.value}"
              )

            