"""Задание 1
Реализуйте класс «Студент». Необходимо хранить в полях класса: ФИО,
дату рождения, название группы, средний балл, предметы. Реализуйте
конструктор по умолчанию и метод для вывода данных объекта. Реализуйте
методы валидации данных для атрибутов объекта. Реализуйте доступ к
отдельным атрибутам класса через методы (геттеры и сеттеры), используя
декоратор @property и @атрибут.setter."""

from Errors import EmptyNameError
from Errors import ValidateIntError
from Errors import ValidateStrError
from Errors import ValidateFormatStrError
from Errors import ValidateFormatIntError
from Errors import ValidateFormatFloatError
from Errors import ValidateFormatBoolError

class Student:
    def __init__(self, name: str, age: int, ):
        ...













"""
Задание 2
Реализуйте класс «Книга». Необходимо хранить в полях класса: название
книги, год выпуска, издателя, жанр, автора, цену. Реализуйте конструктор по
умолчанию и метод для вывода данных объекта. Реализуйте методы
валидации данных для атрибутов объекта. Реализуйте доступ к отдельным
атрибутам класса через методы (геттеры и сеттеры), используя декоратор
@property и @атрибут.setter"""