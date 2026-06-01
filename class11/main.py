# # Example A — plain constants
# STATUS_OPEN = "open"
# STATUS_CLOSED = "closed"
# STATUS_CANCELLED = "cancelled"

# status = STATUS_OPEN
# print(status)

# # Example B — first enum
# from enum import Enum

# class CourseStatus(Enum):
#     OPEN = "open"
#     CLOSED = "closed"
#     CANCELLED = "cancelled"
    
# status = CourseStatus.OPEN
# print(status)
# print(status.value)

# # Example C — comparison
# if status == CourseStatus.OPEN:
#     print("Registration is allowed.")

# # Example D — loop through enum values
# from enum import Enum

# class Priority(Enum):
#     LOW = "low"
#     MEDIUM = "medium"
#     HIGH = "high"

# for priority in Priority:
#     print(priority, priority.value)

from course import Course
from status import CourseStatus
from student import Student

course1 = Course("Advanced Programming", 30, CourseStatus.OPEN)
course2 = Course("Web Interface Programming 2", 25, CourseStatus.CLOSED)
course3 = Course("Web Environment", 20, CourseStatus.CANCELLED)

course1.display_info()
course2.display_info()

course1.close_registration()
course1.display_info()

course2.reopen_course()
course2.display_info()

course3.cancel_course()
course3.reopen_course()

try:
    bad_course = Course("Bad Course", 20, "open")
except ValueError as e:
    print("Error:", e)