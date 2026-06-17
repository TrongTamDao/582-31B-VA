from core.exceptions import InvalidBookingError
from core.enums import ShowStatus
from core.constants import MAX_TICKETS_PER_BOOKING
from models.movie_show import MovieShow
from models.customer import Customer
from models.staff import Staff
from utils import *

def main():
    customer = Customer("Ava")
    show = MovieShow(format_title("Inception"), 20, ShowStatus.OPEN)
    
    print_separator()
    customer.display_info()
    print_separator()
    show.display_info()
    print_separator()
    print("Max tickets per booking:", MAX_TICKETS_PER_BOOKING)
    print_separator()

if __name__ == "__main__":
    main()