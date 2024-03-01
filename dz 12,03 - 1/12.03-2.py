"""Задание 1
Реализуйте класс «Студент». Необходимо хранить в полях класса: ФИО,
дату рождения, название группы, средний балл, предметы. Реализуйте
конструктор по умолчанию и метод для вывода данных объекта. Реализуйте
методы валидации данных для атрибутов объекта. Реализуйте доступ к
отдельным атрибутам класса через методы (геттеры и сеттеры), используя
декоратор @property и @атрибут.setter."""
from datetime import date
from Errors import EmptyNameError
from Errors import ValidateIntError
from Errors import ValidateStrError
from Errors import ValidateFormatStrError
from Errors import ValidateFormatIntError
from Errors import ValidateFormatFloatError

class Student:
    def __init__(self, name: list, date_of_born: date, title_group: str, average_score: float, items: list):
        self.name = self.__validate_name(name)
        self.__date_of_born = self.__validate_date_of_born(date_of_born)
        self.__title_group = self.__validate_title_group(title_group)
        self.__average_score = self.__validate_average_score(average_score)
        self.__items = list
    def __str__(self):
        """Метод для вывода информации всех значений атрибутов на печать"""

        return (f'ФИО: {self.name} \n'
                f'Дата рождения: {self.date_of_born}\n'
                f'Название группы: {self.title_group}\n'
                f'Средний балл: {self.average_score}\n'
                f'Изучаемые предметы: {self.items}\n')

    @staticmethod
    def __validate_name(name: list) -> list:
        """Метод для проверки введенной информации в Параметр "Дата рождения" проверяется на пустое значение,
            проверка на тип вводимых данных (строка), а так же на вводимые символы"""

        if not isinstance(name, list):
            raise ValidateStrError('Параметр "Дата рождения" должен быть списком')
        if not name:
            raise EmptyNameError('Параметр "Дата рождения" не может быть пустым')
        return name

    @staticmethod
    def __validate_date_of_born(date_of_born: date) -> date:
        """Метод для проверки введенной информации в Параметр "Дата рождения" проверяется на пустое значение,
            проверка на тип вводимых данных (строка), а так же на вводимые символы"""

        if not isinstance(date_of_born, date):
            raise ValidateStrError('Параметр "Дата рождения" должен быть числом')
        if not date_of_born:
            raise EmptyNameError('Параметр "Дата рождения" не может быть пустым')
        return date_of_born

    @staticmethod
    def __validate_title_group(title_group: str) -> str:
        """Метод для проверки введенной информации в Параметр "Название группы" проверяется на пустое значение,
            проверка на тип вводимых данных (строка), а так же на вводимые символы"""

        if not isinstance(title_group, str):
            raise ValidateStrError('Параметр "Название группы" должен быть строкой')
        if not title_group:
            raise EmptyNameError('Параметр "Название группы" не может быть пустым')
        a = list(filter(lambda x: 1040 <= ord(x) <= 1103, title_group))
        if len(a) != len(title_group):
            raise ValidateFormatStrError('Параметр "Название группы" должен содержать только символы кириллицы')
        return title_group.capitalize()

    @staticmethod
    def __validate_average_score(average_score: float) -> float:
        """Метод для проверки введенной информации в параметр "Средний балл", проверяется на пустое значение,
                            проверка на тип вводимых данных (целочисленное значение)"""

        if not isinstance(average_score, float):
            raise ValidateFormatFloatError('Параметр "Средний балл" должен быть числом округленным до сотых')
        if not average_score:
            raise EmptyNameError('Средний балл" не может быть пустым')
        return average_score



"""
Задание 2
Реализуйте класс «Книга». Необходимо хранить в полях класса: название
книги, год выпуска, издателя, жанр, автора, цену. Реализуйте конструктор по
умолчанию и метод для вывода данных объекта. Реализуйте методы
валидации данных для атрибутов объекта. Реализуйте доступ к отдельным
атрибутам класса через методы (геттеры и сеттеры), используя декоратор
@property и @атрибут.setter"""