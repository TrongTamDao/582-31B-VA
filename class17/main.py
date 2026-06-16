from exceptions import InvalidBookingError
from enums import ShowStatus
from constants import MAX_TICKETS_PER_BOOKING
from movie_show import MovieShow
from customer import Customer

def main():
    customer = Customer("Ava")
    show = MovieShow("Inception", 20, ShowStatus.OPEN)

    customer.display_info()
    show.display_info()
    print("Max tickets per booking:", MAX_TICKETS_PER_BOOKING)

if __name__ == "__main__":
    main()