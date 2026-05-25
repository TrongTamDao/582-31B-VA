from student_record import StudentRecord
from course_section import CourseSection

def transfer(source_course, target_course):
    if target_course.enrolled >=1 and target_course.enrolled<target_course.capacity:
        target_course.register_student()
        source_course.drop_student()
        print(f"Student was transferred successfully from {source_course.title} to {target_course.title}")
    else:
        print("Trasnfer is not completed")
            
c1 = CourseSection("Advance web programing", 12, 1)
c2 = CourseSection("Web program interface", 14, 14)
transfer(c1, c2)
c1.display_info()
c2.display_info()

# c1.display_info()
# s1.display_info()

# print("==========CourseSection method===========")
# c1.register_student()
# c1.drop_student()

# c1.capacity = 14
# # print(c1.capacity)
# c1.enrolled = 13

# try:
#     s1.update_gpa(5.0)
# except ValueError as e:
#     print("Error:", e)
   
# print(s1.gpa)    
# print(s1.academic_status)