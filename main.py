from datetime import date

from models.student import Student
from models.teacher import Teacher


student1 = Student(
    "joel", date(2003, 12, 1), "Içara", 1, "informática", [8, 6]
)

student2 = Student(
    "Eduardo", date(2003, 4, 12), "Porto Alegre", 2, "informática", [9, 7]
)

teacher1 = Teacher(
    "Marcio",
    date(1986, 8, 23),
    "Criciúma",
    2,
    "Matemática",
    "Matemática-terceiro-ano",
)

# print(student1.calculate_average_grade())
# print(student1)
# print(student2)
# print(teacher1)
teacher1.take_attendance(student1, student2)
# student1.answer_attendance()
print(teacher1.close_averages(student1, student2))
averages = teacher1.close_averages_with_accessable_name(student1, student2)
for x in averages:
    print(f"{x}: {averages[x]}")
