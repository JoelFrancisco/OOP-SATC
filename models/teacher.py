from datetime import date
from collections import namedtuple

from .person import Person


class Teacher(Person):
    def __init__(self, name, date_of_birth: date, address,
                 employee_id, course, subject):
        super().__init__(name, date_of_birth, address)
        self.employee_id = employee_id
        self.course = course
        self.subject = subject

    def take_attendance(self, *students):
        print("taking attendance")
        for student in students:
            print(f'{student.name}? ')
            student.answer_attendance()

    def close_averages(self, *students):
        averages_tuple = namedtuple('Averages', list([student.name for
                                    student in students]))
        averages = averages_tuple(*[student.calculate_average_grade() for
                                    student in students])
        print("closing averages")
        return averages

    def close_averages_with_accessable_name(self, *students):
        averages = {
            student.name: student.calculate_average_grade() for
            student in students
        }
        print("closing averages")
        return averages

    def __str__(self):
        printable = super().__str__()
        printable += f"ID do professor: {self.employee_id}\n"
        printable += f"Curso: {self.course}\n"
        printable += f"Disciplina: {self.subject}\n"
        return printable
