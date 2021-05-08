from datetime import date


class Person:
    def __init__(self, name, date_of_birth: date, address):
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address

    def __str__(self):
        printable = f"Nome: {self.name}\n"
        printable += f"Data de nascimento: {self.date_of_birth}\n"
        printable += f"Endereço: {self.address}\n"
        return printable
