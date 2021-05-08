from datetime import date

from .person import Person


class Teacher(Person):
    def __init__(self, name, date_of_birth: date, address, employee_id, course, subject):
        super().__init__(name, date_of_birth, address)
        self.employee_id = employee_id
        self.course = course
        self.subject = subject

    def take_attendance(self):
        return print("taking attendance")

    def close_averages(self, *students):
        averages = [student.calculate_average_grade() for student in students]
        print("closing averages")
        return averages

    def __str__(self):
        printable = super().__str__()
        printable += f"ID do professor: {self.employee_id}\n"
        printable += f"Curso: {self.course}\n"
        printable += f"Disciplina: {self.subject}\n"
        return printable