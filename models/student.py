from datetime import date

from .person import Person


class Student(Person):
    def __init__(self, name, date_of_birth: date,
                 address, id, course, grades=[0]):
        super().__init__(name, date_of_birth, address)
        self.id = id
        self.course = course
        self.grades = grades
        self.average = self.calculate_average_grade()

    def calculate_average_grade(self) -> float:
        average = sum(self.grades) / len(self.grades)
        return average

    def answer_attendance(self):
        print(f"{self.name} answering attendance")

    def __str__(self):
        printable = super().__str__()
        printable += f"ID do aluno: {self.id}\n"
        printable += f"Curso: {self.course}\n"
        printable += f"Notas: {self.grades}\n"
        printable += f"Média: {self.average}\n"
        return printable
