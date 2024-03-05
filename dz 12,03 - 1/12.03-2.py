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
from Errors import ValidateFormatStrError

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
        """Метод для проверки введенной информации в Параметр "ФИО" проверяется на пустое значение,
            проверка на тип вводимых данных (строка), а так же на вводимые символы"""

        if not isinstance(name, list):
            raise ValidateStrError('Параметр "ФИО" должен быть списком')
        if not name:
            raise EmptyNameError('Параметр "ФИО" не может быть пустым')
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
    def __validate_items(items: str) -> list:
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

    def append_items(self, items: str):
        """Метод для добавления нового предмета в список предметов."""

        if items in self.__items:
            raise Exception('Ошибка повторного добавления элемента')
        if not isinstance(items, str):
            raise ValidateStrError('Добавляемый параметр должен быть строкой')
        else:
            self.__items.append(items)



student1 = Student(['Иванов', 'Иван', 'Иванович'], date(1984, 4, 9), 'П-7', 4.4, ['Математика',"Физика", "Высшая математика"])
print(student1.name)
student1.name = ['Петров', 'Петр', 'Петрович']
print(student1.name)
student1.append_items('Тригонометрия')
print(student1.items)




"""
Задание 2
Реализуйте класс «Книга». Необходимо хранить в полях класса: название
книги, год выпуска, издателя, жанр, автора, цену. Реализуйте конструктор по
умолчанию и метод для вывода данных объекта. Реализуйте методы
валидации данных для атрибутов объекта. Реализуйте доступ к отдельным
атрибутам класса через методы (геттеры и сеттеры), используя декоратор
@property и @атрибут.setter"""

from datetime import date

class Book:
    """Класс 'Книга' описывает книги и их параметры. Класс имеет следующие атрибуты:
        - title_book - Название книги
        - year_of_release - год выпуска
        - publisher - Издатель
        - genre - жанр
        - autor - Автор
        - price - цена
        Так же класс имеет следующие методы:
        - статик-методы (validate_атрибут) для валидации атрибутов
        - свойства атрибутов (@property) для их вывода
        - сеттеры атрибутов (@атрибут.setter) для изменения значений атрибутов"""
    def __init__(self, title_book: str, year_of_release: date, publisher: str, genre: str, autor: str, price: float):
        self.__title_book = self.__validate_title_book(title_book)
        self.__year_of_release = self.__validate_year_of_release(year_of_release)
        self.__publisher = self.__validate_publisher(publisher)
        self.__genre = self.__validate_genre(genre)
        self.__autor = self.__validate_autor(autor)
        self.__price = self.__validate_price(price)

    def __str__(self):
        """Метод для вывода информации всех значений атрибутов на печать"""
        return (f'Название книги: {self.__title_book}\n'
                f'Год выпуска: {self.__year_of_release}\n'
                f'Издатель: {self.__publisher}\n'
                f'Жанр: {self.__genre} \n'
                f'Автор: {self.__autor} \n'
                f'Цена книги: {self.__price}')

    @staticmethod
    def __validate_title_book(title_book: str) -> str:
        """Метод для проверки введенной информации в Параметр "Название книги" проверяется на пустое значение,
            проверка на тип вводимых данных (строка), а так же на вводимые символы """

        if not isinstance(title_book, str):
            raise ValidateStrError('Параметр "Название книги" должен быть строкой')
        if not title_book:
            raise EmptyNameError('Параметр "Название книги" не может быть пустым')
        q = list(filter(lambda x: 1040 <= ord(x) <= 1103, title_book))
        if len(q) != len(title_book):
            raise ValidateFormatStrError('Параметр "Издатель" может содержать символы кириллицы, '
                                         'цифры и английский алфавит')
        return title_book

    @staticmethod
    def __validate_year_of_release(year_of_release: date) -> date:
        """Метод для проверки введенной информации в Параметр "Год выпуска" проверяется на пустое значение,
            проверка на тип вводимых данных (дата)"""

        if not year_of_release:
            raise EmptyNameError('Параметр "Год выпуска" не может быть пустым')
        return year_of_release

    @staticmethod
    def __validate_publisher(publisher: str) -> str:
        """Метод для проверки введенной информации в Параметр "Издатель" проверяется на пустое значение,
            проверка на тип вводимых данных (строка), а так же на вводимые символы"""

        if not isinstance(publisher, str):
            raise ValidateStrError('Параметр "Издатель" должен быть строкой')
        if not publisher:
            raise EmptyNameError('Параметр "Издатель" не может быть пустым')
        a = list(filter(lambda x: 1040 <= ord(x) <= 1103, publisher))
        if len(a) != len(publisher):
            raise ValidateFormatStrError('Параметр "Издатель" может содержать символы кириллицы, '
                                         'цифры и английский алфавит')
        return publisher.capitalize()

    @staticmethod
    def __validate_genre(genre: str) -> str:
        """Метод для проверки введенной информации в Параметр "Жанр" проверяется на пустое значение,
                    проверка на тип вводимых данных (строка), а так же на вводимые символы"""

        if not isinstance(genre, str):
            raise ValidateFormatFloatError('Параметр "Жанр" должен быть строкой')
        if not genre:
            raise EmptyNameError('Параметр "Жанр" не может быть пустым')
        a = list(filter(lambda x: 1040 <= ord(x) <= 1103, genre))
        if len(a) != len(genre):
            raise ValidateFormatStrError('Параметр "Жанр" может содержать символы кириллицы, '
                                         'цифры и английский алфавит')
        return genre

    @staticmethod
    def __validate_autor(autor: str) -> str:
        """Метод для проверки введенной информации в Параметр "Автор" проверяется на пустое значение,
            проверка на тип вводимых данных (строка), а так же на вводимые символы"""
        if not isinstance(autor, str):
            raise ValidateStrError('Параметр "Автор" должен быть списком')
        if not autor:
            raise EmptyNameError('Параметр "Автор" не может быть пустым')
        a = list(filter(lambda x: 1040 <= ord(x) <= 1103, autor))
        if len(a) != len(autor):
            raise ValidateFormatStrError('Параметр "Автор" может содержать символы кириллицы, '
                                         'цифры и английский алфавит')
        return autor

    @staticmethod
    def __validate_price(price: float) -> float:
        """Метод для проверки введенной информации в параметр "Цена", проверяется на пустое значение,
                            проверка на тип вводимых данных (число округленное до сотых)"""

        if not isinstance(price, float):
            raise ValidateFormatFloatError('Параметр "Цена" должен быть числом округленным до сотых')
        if not price:
            raise EmptyNameError('Параметр "Цена" не может быть пустым')
        return price

    @property
    def title_book(self) -> str:
        return self.__title_book

    @title_book.setter
    def title_book(self, title_book):
        self.__title_book = self.__validate_title_book(title_book)

    @property
    def year_of_release(self) -> date:
        return self.__year_of_release

    @year_of_release.setter
    def year_of_release(self, year_of_release):
        self.__year_of_release = self.__validate_year_of_release(year_of_release)

    @property
    def publisher(self) -> str:
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher):
        self.__publisher = self.__validate_publisher(publisher)

    @property
    def genre(self) -> str:
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = self.__validate_genre(genre)

    @property
    def autor(self) -> str:
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = self.__validate_autor(autor)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = self.__validate_price(price)


book1 = Book('Сказки', (1984, 5, 21), 'Сфера', 'Развлекательный', 'Пушкин', 3.62)
print(book1)
