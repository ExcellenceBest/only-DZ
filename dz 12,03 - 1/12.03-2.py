"""Задание 1
Реализуйте класс «Студент». Необходимо хранить в полях класса: ФИО,
дату рождения, название группы, средний балл, предметы. Реализуйте
конструктор по умолчанию и метод для вывода данных объекта. Реализуйте
методы валидации данных для атрибутов объекта. Реализуйте доступ к
отдельным атрибутам класса через методы (геттеры и сеттеры), используя
декоратор @property и @атрибут.setter."""
from datetime import date
from Errors import EmptyNameError
from Errors import ValidateStrError
from Errors import ValidateFormatFloatError

class Student:
    def __init__(self, name: list, date_of_born: date, title_group: str, average_score: float, items: list):
        self.name = self.__validate_name(name)
        self.__date_of_born = self.__validate_date_of_born(date_of_born)
        self.__title_group = self.__validate_title_group(title_group)
        self.__average_score = self.__validate_average_score(average_score)
        self.__items = self.__validate_items(items)

    def __str__(self):
        """Метод для вывода информации всех значений атрибутов на печать"""

        return (f'ФИО: {self.name} \n'
                f'Дата рождения: {self.__date_of_born}\n'
                f'Название группы: {self.__title_group}\n'
                f'Средний балл: {self.__average_score}\n'
                f'Изучаемые предметы: {self.__items}\n')

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

    @staticmethod
    def __validate_items(items: list) -> list:
        """Метод для проверки введенной информации в Параметр "Изучаемые предметы" проверяется на пустое значение,
            проверка на тип вводимых данных (строка), а так же на вводимые символы"""

        if not isinstance(items, list):
            raise ValidateStrError('Параметр "Изучаемые предметы" должен быть списком')
        if not items:
            raise EmptyNameError('Параметр "Изучаемые предметы" не может быть пустым')
        return items

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = self.__validate_name(name)

    @property
    def date_of_born(self) -> date:
        return self.__date_of_born

    @date_of_born.setter
    def date_of_born(self, date_of_born):
        self.__date_of_born = self.__validate_date_of_born(date_of_born)

    @property
    def title_group(self) -> str:
        return self.__title_group

    @title_group.setter
    def title_group(self, title_group):
        self.__title_group = self.__validate_title_group(title_group)

    @property
    def average_score(self) -> float:
        return self.__average_score

    @average_score.setter
    def average_score(self, average_score):
        self.__average_score = self.__validate_average_score(average_score)

    @property
    def items(self) -> list:
        return self.__items

    @items.setter
    def items(self, items):
        self.__items = self.__validate_items(items)


student1 = Student(['Иванов', 'Иван', 'Иванович'], date(1984, 4, 9), 'П-7', 4.4, ['Математика',"Физика", "Высшая математика"])
print(student1)
student1.items = ['Тригонометрия']
print(student1.items)
"""


Задание 2
Реализуйте класс «Книга». Необходимо хранить в полях класса: название
книги, год выпуска, издателя, жанр, автора, цену. Реализуйте конструктор по
умолчанию и метод для вывода данных объекта. Реализуйте методы
валидации данных для атрибутов объекта. Реализуйте доступ к отдельным
атрибутам класса через методы (геттеры и сеттеры), используя декоратор
@property и @атрибут.setter"""