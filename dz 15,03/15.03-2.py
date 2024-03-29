""" Задание 1.
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

from datetime import date, datetime

class Human:
    """ Класс "Человек" описывает человека.
        Attributes:
        - name: list  - Фамилия , Имя , Отчество
        - date_of_born: date - Дата рождения
        - telephone: str - Номер телефона
        Methods:
        - create_human_alternative - метод класса для создания объекта альтернативным способом
         - lived_through  - метод для вычисления возраста. """

    def __init__(self, name: list, age: int, telephone: str):
        self.__name = name
        self.__age = age
        self.__telephone = telephone

    @classmethod
    def create_human_alternative(cls, name: list, age: int, telephone: str) -> object:
        """Метод позволяет создавать экземпляры класса альтернативным способом,
        принимает в себя параметр name, age, telephone и возвращает объект класса."""

        return cls(name, age, telephone)

    def __str__(self):
        """Метод для вывода информации всех значений атрибутов на печать"""
        self.__name = " ".join(str(i) for i in self.__name)
        return (f'ФИО: {self.__name}\n'
                f'Возраст: {self.__age}\n'
                f'Телефон: {self.__telephone}')

    @property
    def name(self) -> list:
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def telephone(self) -> str:
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone):
        self.__telephone = telephone

    @staticmethod
    def lived_through(date_of_born: date):
        now = date.today()
        human_birthday = date_of_born
        age = now.year - human_birthday.year
        return f'Возраст объекта {age} лет\n'


human1 = Human(['Иванов', 'Иван', 'Иванович'], date(1984, 9, 4), '+7-964-136-5667')
print(human1)
print(human1.lived_through(date(1984, 4, 9)))
human2 = Human.create_human_alternative(["Бодров", "Сергей", "Андреевич"], date(1999, 2, 4), "8-999-345-23-23")
print(human2)

"""Задание 2
Реализуйте класс «Книга».
Необходимо хранить в полях класса: название, жанр, год публикации.
Реализуйте конструктор по умолчанию и метод для вывода данных.
Реализуйте доступ к отдельным полям класса через методы класса (геттеры
и сеттеры).
Реализуйте метод класса, который принимает в качестве параметра
путь к файлу где содержится информация о книге. Создайте экземпляр класса
используя альтернативный конструктор.
Добавьте классу статическую переменную, которая хранит тип
экземпляра книги. По умолчанию все объекты должны создаваться с типом
«Бумажный экземпляр». Реализуйте метод, который изменяет для отдельного
объекта тип на «Электронный экземпляр»."""


class Book:
    """Класс 'Книга' описывает книги и их параметры.
        Attributes:
        - title_book: str - Название книги
        - genre: str - жанр
        - year_of_release: date - год выпуска
        Methods:
        - type_of_book -  получение данных о типе экземпляра книги
        - change_type_of_book - изменение типа экземпляра книги """


    _type_book = 'Бумажный'

    def __init__(self, title_book: str, genre: str, year_of_release: str):
        self.__title_book = title_book
        self.__genre = genre
        self.__year_of_release = year_of_release

    def __str__(self):
        """Метод для вывода информации всех значений атрибутов на печать"""
        return (f'Название книги: {self.__title_book}\n'
                f'Жанр: {self.__genre} \n'
                f'Год выпуска: {self.__year_of_release}')

    @classmethod
    def create_book_alternative(cls, path: str) -> object:
        """Метод позволяет создавать экземпляры класса альтернативным способом,
        принимает в себя параметр path: str(путь к файлу) и возвращает объект класса."""
        with open(path, 'r', encoding='utf-8') as file:
            create_book = list(map(lambda x: x.rstrip('\n'), file.readlines()))
            datetime.strptime(create_book[2], '%Y-%m-%d')
            _type_book = Book._type_book
            print(_type_book)
        return cls(*create_book)

    @property
    def type_of_book(self) -> str:
        return f'Ваш экземпляр книги: {self._type_book}\n'


    def change_type_of_book(self, value: str):
        self._type_book = value

    @property
    def title_book(self) -> str:
        return self.__title_book

    @title_book.setter
    def title_book(self, title_book):
        self.__title_book = title_book

    @property
    def genre(self) -> str:
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    @property
    def year_of_release(self) -> date:
        return self.__year_of_release

    @year_of_release.setter
    def year_of_release(self, year_of_release):
        self.__year_of_release = year_of_release


book1 = Book('Сказки', 'Развлекательный', date(1999,  12, 6))
print(book1)
print(book1.type_of_book)
book1.change_type_of_book('Электронный')
print(book1.type_of_book)
print('__________________________________________________________')
book2 = Book.create_book_alternative('book.txt')
print(book2)
print(book2.type_of_book)
book2.change_type_of_book('Электронный')
print(book2.type_of_book)
print('__________________________________________________________')
book3 = Book('Комиксы', 'Развлекательный', date(2003, 4, 8))
print(book3)
print(book3.type_of_book)
book3.change_type_of_book('Электронный')
print(book3.type_of_book)
