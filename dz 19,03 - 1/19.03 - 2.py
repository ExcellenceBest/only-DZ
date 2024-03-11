"""Задание 1.
Создайте класс Human, который будет содержать информацию о
человеке. С помощью механизма наследования, реализуйте класс Builder
(содержит информацию о строителе), класс Sailor (содержит информацию о
моряке), класс Pilot (содержит информацию о летчике). Каждый из классов
должен содержать необходимые для работы методы."""
from datetime import date
class Human:
    """ Класс "Человек" описывает человека. Класс имеет атрибуты такие как:
        - name - ФИО
        - date_of_born - Дата рождения
        - telephone - Номер телефона
        Так же класс имеет следующие методы:
        - свойства атрибутов (@property) для их вывода
        - сеттеры атрибутов (@атрибут.setter) для изменения значений атрибутов """

    def __init__(self, name: list, date_of_born: date, telephone: str):
        self.__name = name
        self.__date_of_born = date_of_born
        self.__telephone = telephone


    def __str__(self):
        """Метод для вывода информации всех значений атрибутов на печать"""
        self.name = " ".join(str(i) for i in self.__name)
        return (f'ФИО: {self.name}\n'
                f'Дата рождения: {self.__date_of_born}\n'
                f'Телефон: {self.__telephone}')

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


class Builder(Human):
    """ Класс "Строитель" описывает строителя. Класс имеет атрибуты такие как:
            - name - ФИО
            - date_of_born - Дата рождения
            - telephone - Номер телефона
            - post - Должность
            Так же класс имеет следующие методы:
            - свойства атрибутов (@property) для их вывода
            - сеттеры атрибутов (@атрибут.setter) для изменения значений атрибутов """
    def __init__(self, name: list, date_of_born: date, telephone: str, post: str):
        super().__init__(name, date_of_born, telephone)
        self.__post = post

    @property
    def post(self) -> str:
        return f'Должность: {self.__post}\n'

    @post.setter
    def post(self, post):
        self.__post = post


class Sailor(Human):
    """ Класс "Моряк" описывает моряка. Класс имеет атрибуты такие как:
                - name - ФИО
                - date_of_born - Дата рождения
                - telephone - Номер телефона
                - rank - Звание
                Так же класс имеет следующие методы:
                - свойства атрибутов (@property) для их вывода
                - сеттеры атрибутов (@атрибут.setter) для изменения значений атрибутов """
    def __init__(self, name: list, date_of_born: date, telephone: str, rank: str):
        super().__init__(name, date_of_born, telephone)
        self.__rank = rank

    @property
    def rank(self) -> str:
        return f'Звание: {self.__rank}\n'

    @rank.setter
    def rank(self, rank):
        self.__rank = rank

class Pilot(Human):
    """ Класс "Пилот" описывает пилота. Класс имеет атрибуты такие как:
                - name - ФИО
                - date_of_born - Дата рождения
                - telephone - Номер телефона
                - flight_experience - Летный опыт
                Так же класс имеет следующие методы:
                - свойства атрибутов (@property) для их вывода
                - сеттеры атрибутов (@атрибут.setter) для изменения значений атрибутов """
    def __init__(self, name: list, date_of_born: date, telephone: str, flight_experience: int):
        super().__init__(name, date_of_born, telephone)
        self.__flight_experience = flight_experience

    @property
    def flight_experience(self) -> str:
        return f'Летный опыт: {self.__flight_experience} лет\n'

    @flight_experience.setter
    def flight_experience(self, flight_experience):
        self.__flight_experience = flight_experience



human1 = Human(['Земляникин', 'Геннадий', 'Петрович'], date(1984, 9, 4), '+7-964-136-5667')
print(f'{human1}\n')
builder1 = Builder(['Климушкин', 'Василий', 'Иванович'], date(1994, 4, 12),
                   '+7-998-345-3423', 'Прораб')
print(builder1)
print(builder1.post)
sailor1 = Sailor(['Карпов', 'Юрий', 'Иванович'], date(1985, 8, 24),
                 '+7-964-136-3456', 'Капитан 1 ранга')
print(sailor1)
print(sailor1.rank)
pilot1 = Pilot(['Гагарин', 'Юрий', 'Алексеевич'], date(1934, 9, 3),
               'None', 4)
print(pilot1)
print(pilot1.flight_experience)


"""Задание 2
Создайте класс Passport (паспорт), который будет содержать
паспортную информацию о гражданине заданной страны. С помощью
механизма наследования, реализуйте класс ForeignPassport (загран.паспорт)
производный от Passport. Напомним, что заграничный паспорт содержит помимо паспортных данных, 
также данные о визах, номер заграничного
паспорта."""


class Passport:
    """ Класс "Паспорт" описывает паспорт. Класс имеет атрибуты такие как:
                    - name - ФИО
                    - date_of_born - Дата рождения
                    - telephone - Номер телефона
                    - address - Адрес проживания
                    Так же класс имеет следующие методы:
                    - свойства атрибутов (@property) для их вывода
                    - сеттеры атрибутов (@атрибут.setter) для изменения значений атрибутов """
    def __init__(self, name: list, date_of_born: date, passport_series_number: int, address: str):
        self.__name = name
        self.__date_of_born = date_of_born
        self.__passport_series_number = passport_series_number
        self.__address = address

    def __str__(self):
        """Метод для вывода информации всех значений атрибутов на печать"""
        self.name = " ".join(str(i) for i in self.__name)
        return (f'ФИО: {self.__name}\n'
                f'Дата рождения: {self.__date_of_born}\n'
                f'Серия и номер паспорта: {self.__passport_series_number}\n'
                f'Адрес проживания: {self.__address}')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def date_of_born(self):
        return self.__date_of_born

    @date_of_born.setter
    def date_of_born(self, date_of_born):
        self.__date_of_born = date_of_born

    @property
    def passport_series_number(self):
        return self.__passport_series_number

    @passport_series_number.setter
    def passport_series_number(self, passport_series_number):
        self.__passport_series_number = passport_series_number

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address


class ForeignPassport(Passport):
    """ Класс "Загран-паспорт" описывает загран-паспорт. Класс имеет атрибуты такие как:
                        - name - ФИО
                        - date_of_born - Дата рождения
                        - telephone - Номер телефона
                        - address - Адрес проживания
                        - number_foreign_passport - серийный номер загран-паспорта
                        - visa - Одобренная виза
                        Так же класс имеет следующие методы:
                        - свойства атрибутов (@property) для их вывода
                        - сеттеры атрибутов (@атрибут.setter) для изменения значений атрибутов """
    def __init__(self, name: list, date_of_born: date, passport_series_number: int, address: str,
                 number_foreign_passport: int, visa: str):
        super().__init__(name, date_of_born, passport_series_number, address)
        self.__number_foreign_passport = number_foreign_passport
        self.__visa = visa

    @property
    def number_foreign_passport(self):
        return f'Номер загранпаспорта: {self.__number_foreign_passport}'

    @number_foreign_passport.setter
    def number_foreign_passport(self, number_foreign_passport):
        self.__number_foreign_passport = number_foreign_passport

    @property
    def visa(self):
        return f'Текущая рабочая виза: {self.__visa}'

    @visa.setter
    def visa(self, visa):
        self.__visa = visa

foreign_passport1 = ForeignPassport(['Путин', 'Владимир', 'Владимирович'],
                                    date(1955, 9, 4), 7808665644,
                                    'Рыбная улица, 4', 2388492, 'Шенген')
print(foreign_passport1)
print(foreign_passport1.number_foreign_passport)
print(foreign_passport1.visa)
