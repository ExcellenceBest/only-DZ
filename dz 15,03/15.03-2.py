"""Задание 1.
Реализуйте класс «Человек».
Необходимо хранить в полях класса: ФИО, возраст, контактный
телефон. Реализуйте конструктор по умолчанию и метод для вывода данных.
Реализуйте доступ к отдельным полям класса через методы класса (геттеры
и сеттеры).
Реализуйте метод класса, который принимает в качестве параметров
ФИО, дату рождения (день, месяц, год), контактный телефон. Создайте
экземпляр класса используя альтернативный конструктор.
Реализуйте статический метод, который вычисляет возраст человека
относительно текущего дня по переданной дате рождения """
from datetime import datetime, date, time

class Human:
    """Класс "Человек" описывает человека. Класс имеет атрибуты такие как:
        - name - ФИО
        - date_of_born - Дата рождения
        - telephone - Номер телефона
        Так же класс имеет следующие методы:
        - свойства атрибутов (@property) для их вывода
        - сеттеры атрибутов (@атрибут.setter) для изменения значений атрибутов
        - create_human_alternative - класс-метод для создания объекта """
    def __init__(self, name: list, date_of_born: date, telephone: str):
        self.__name = name
        self.__date_of_born = date_of_born
        self.__telephone = telephone

    @classmethod
    def create_human_alternative(cls, path: str) -> object:
        """Метод позволяет создавать экземпляры класса альтернативным способом,
                    принимает в себя параметр path: str(путь к файлу)
                    и возвращает объект класса."""
        with open(path, 'r', encoding='utf-8') as file:
            create_human = list(map(lambda x: x.rstrip('\n'), file.readlines()))
            print(create_human)
            create_human[1] = create_human[1]
            create_human[2] = str(create_human[2])

        return cls(*create_human)


    def __str__(self):
        """Метод для вывода информации всех значений атрибутов на печать"""

        return (f'ФИО: {self.name} \n'
                f'Дата рождения: {self.__date_of_born}\n'
                f'Телефон: {self.__telephone}\n')

    @property
    def name(self) -> list:
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def date_of_born(self) -> date:
        return self.__date_of_born

    @date_of_born.setter
    def date_of_born(self, date_of_born):
        self.__date_of_born = date_of_born

    @property
    def telephone(self) -> str:
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone):
        self.__telephone = telephone

    @staticmethod
    def lived_through(born):
        now = date.today()
        date_born = date()
        result = now - born
        return result


human1 = Human(['Иванов', 'Иван', 'Иванович'], (1984, 9, 4), '+7-964-136-5667')
print(human1)
human2 = Human.create_human_alternative('Human.txt')
print(human2)
print(human1.lived_through((1984,5,4)))


birthdate = date(2000, 1, 1)
today = date.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))









#
# class Book:
#     """Класс 'Книга' описывает книги и их параметры. Класс имеет следующие атрибуты:
#         - title_book - Название книги
#         - year_of_release - год выпуска
#         - publisher - Издатель
#         - genre - жанр
#         - autor - Автор
#         - price - цена
#         Так же класс имеет следующие методы:
#         - статик-методы (validate_атрибут) для валидации атрибутов
#         - свойства атрибутов (@property) для их вывода
#         - сеттеры атрибутов (@атрибут.setter) для изменения значений атрибутов"""
#     def __init__(self, title_book: str, year_of_release: date, publisher: str, genre: str, autor: str, price: float):
#         self.__title_book = self.__validate_title_book(title_book)
#         self.__year_of_release = self.__validate_year_of_release(year_of_release)
#         self.__publisher = self.__validate_publisher(publisher)
#         self.__genre = self.__validate_genre(genre)
#         self.__autor = self.__validate_autor(autor)
#         self.__price = self.__validate_price(price)
#
#     def __str__(self):
#         """Метод для вывода информации всех значений атрибутов на печать"""
#         return (f'Название книги: {self.__title_book}\n'
#                 f'Год выпуска: {self.__year_of_release}\n'
#                 f'Издатель: {self.__publisher}\n'
#                 f'Жанр: {self.__genre} \n'
#                 f'Автор: {self.__autor} \n'
#                 f'Цена книги: {self.__price}')
#
#     @staticmethod
#     def __validate_title_book(title_book: str) -> str:
#         """Метод для проверки введенной информации в Параметр "Название книги" проверяется на пустое значение,
#             проверка на тип вводимых данных (строка), а так же на вводимые символы """
#
#         if not isinstance(title_book, str):
#             raise ValidateStrError('Параметр "Название книги" должен быть строкой')
#         if not title_book:
#             raise EmptyNameError('Параметр "Название книги" не может быть пустым')
#         q = list(filter(lambda x: 1040 <= ord(x) <= 1103, title_book))
#         if len(q) != len(title_book):
#             raise ValidateFormatStrError('Параметр "Издатель" может содержать символы кириллицы, '
#                                          'цифры и английский алфавит')
#         return title_book
#
#     @staticmethod
#     def __validate_year_of_release(year_of_release: date) -> date:
#         """Метод для проверки введенной информации в Параметр "Год выпуска" проверяется на пустое значение,
#             проверка на тип вводимых данных (дата)"""
#
#         if not year_of_release:
#             raise EmptyNameError('Параметр "Год выпуска" не может быть пустым')
#         return year_of_release
#
#     @staticmethod
#     def __validate_publisher(publisher: str) -> str:
#         """Метод для проверки введенной информации в Параметр "Издатель" проверяется на пустое значение,
#             проверка на тип вводимых данных (строка), а так же на вводимые символы"""
#
#         if not isinstance(publisher, str):
#             raise ValidateStrError('Параметр "Издатель" должен быть строкой')
#         if not publisher:
#             raise EmptyNameError('Параметр "Издатель" не может быть пустым')
#         a = list(filter(lambda x: 1040 <= ord(x) <= 1103, publisher))
#         if len(a) != len(publisher):
#             raise ValidateFormatStrError('Параметр "Издатель" может содержать символы кириллицы, '
#                                          'цифры и английский алфавит')
#         return publisher.capitalize()
#
#     @staticmethod
#     def __validate_genre(genre: str) -> str:
#         """Метод для проверки введенной информации в Параметр "Жанр" проверяется на пустое значение,
#                     проверка на тип вводимых данных (строка), а так же на вводимые символы"""
#
#         if not isinstance(genre, str):
#             raise ValidateFormatFloatError('Параметр "Жанр" должен быть строкой')
#         if not genre:
#             raise EmptyNameError('Параметр "Жанр" не может быть пустым')
#         a = list(filter(lambda x: 1040 <= ord(x) <= 1103, genre))
#         if len(a) != len(genre):
#             raise ValidateFormatStrError('Параметр "Жанр" может содержать символы кириллицы, '
#                                          'цифры и английский алфавит')
#         return genre
#
#     @staticmethod
#     def __validate_autor(autor: str) -> str:
#         """Метод для проверки введенной информации в Параметр "Автор" проверяется на пустое значение,
#             проверка на тип вводимых данных (строка), а так же на вводимые символы"""
#         if not isinstance(autor, str):
#             raise ValidateStrError('Параметр "Автор" должен быть списком')
#         if not autor:
#             raise EmptyNameError('Параметр "Автор" не может быть пустым')
#         a = list(filter(lambda x: 1040 <= ord(x) <= 1103, autor))
#         if len(a) != len(autor):
#             raise ValidateFormatStrError('Параметр "Автор" может содержать символы кириллицы, '
#                                          'цифры и английский алфавит')
#         return autor
#
#     @staticmethod
#     def __validate_price(price: float) -> float:
#         """Метод для проверки введенной информации в параметр "Цена", проверяется на пустое значение,
#                             проверка на тип вводимых данных (число округленное до сотых)"""
#
#         if not isinstance(price, float):
#             raise ValidateFormatFloatError('Параметр "Цена" должен быть числом округленным до сотых')
#         if not price:
#             raise EmptyNameError('Параметр "Цена" не может быть пустым')
#         return price
#
#     @property
#     def title_book(self) -> str:
#         return self.__title_book
#
#     @title_book.setter
#     def title_book(self, title_book):
#         self.__title_book = self.__validate_title_book(title_book)
#
#     @property
#     def year_of_release(self) -> date:
#         return self.__year_of_release
#
#     @year_of_release.setter
#     def year_of_release(self, year_of_release):
#         self.__year_of_release = self.__validate_year_of_release(year_of_release)
#
#     @property
#     def publisher(self) -> str:
#         return self.__publisher
#
#     @publisher.setter
#     def publisher(self, publisher):
#         self.__publisher = self.__validate_publisher(publisher)
#
#     @property
#     def genre(self) -> str:
#         return self.__genre
#
#     @genre.setter
#     def genre(self, genre):
#         self.__genre = self.__validate_genre(genre)
#
#     @property
#     def autor(self) -> str:
#         return self.__autor
#
#     @autor.setter
#     def autor(self, autor):
#         self.__autor = self.__validate_autor(autor)
#
#     @property
#     def price(self) -> float:
#         return self.__price
#
#     @price.setter
#     def price(self, price):
#         self.__price = self.__validate_price(price)
#
#
# book1 = Book('Сказки', (1984, 5, 21), 'Сфера', 'Развлекательный', 'Пушкин', 3.62)
# print(book1)
