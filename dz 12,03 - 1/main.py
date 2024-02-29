"""Задание 1.
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
название модели, год выпуска, производителя, объем двигателя, цвет машины,
цену. Реализуйте конструктор по умолчанию и метод для вывода данных
объекта. Реализуйте методы валидации данных для атрибутов объекта.
Реализуйте доступ к отдельным атрибутам класса через методы объекта
(геттеры и сеттеры), используя декоратор @property и @атрибут.setter."""

from Errors import EmptyNameError
from Errors import ValidateIntError
from Errors import ValidateStrError
from Errors import ValidateFormatStrError
from Errors import ValidateFormatIntError
from Errors import ValidateFormatFloatError
from Errors import ValidateFormatBoolError

class Auto:
    """
    Класс Авто описывает автомобили, их цвета, марки, модели, характеристики
    год выпуска, цена и время разгона до 100 км.ч
    - Атрибуты класса : mark, model, year_of_production, color, price, equipment, acceleration.
    Класс в себе содержит следующие методы:
        - статик-методы (validate_атрибут) для валидации атрибутов
        - свойства атрибутов (@property) для их вывода
        - сеттеры атрибутов (@атрибут.setter) для изменеия значений атрибутов
    """
    equip_auto = {'Коробка передач': "automat", 'Электропакет': "full", 'Тип': "petrol",
            'Объем двигателя':  1.5, 'Производитель': 'Korea'}
    def __init__(self, mark: str, model: str, year_of_production: int, color: str, price: float,
                 equipment: dict, acceleration: float):
        self.__mark = self.__validate_mark(mark)
        self.__model = self.__validate_model(model)
        self.__year_of_production = self.__validate_year_of_production(year_of_production)
        self.__color = self.__validate_color(color)
        self.__price = self.__validate_price(price)
        self.__equipment = self.__validate_equipment(equipment)
        self.__acceleration = self.__validate_acceleration(acceleration)

    def __str__(self):
        """Метод для вывода инвормации всех значений атрибутов на печать"""

        return (f'Марка Авто: {self.mark} \n'
                f'Модель Авто: {self.model}\n'
                f'Год выпуска: {self.year_of_production}\n'
                f'Цвет кузова Авто: {self.color}\n'
                f'Цена Авто: {self.price}\n'
                f'Комплектация Авто: {self.equipment}\n'
                f'Разгон до 100 км/ч,сек: {self.acceleration}')

    @staticmethod
    def __validate_mark(mark: str) -> str:
        """Метод для проверки введенной информации в поле "марка авто", проверяется на пустое значение,
            присутствие цифр, проверка на тип вводимых данных (строка), а так же на вводимые символы"""

        if not isinstance(mark, str):
            raise ValidateStrError('Параметр "Марка Авто" должен быть строкой')
        if not mark:
            raise EmptyNameError('Параметр "Марка Авто" не может быть пустым')
        if mark.isdigit():
            raise ValidateFormatStrError('Параметр "Марка Авто" не может быть цифр')
        a = list(filter(lambda x: 48 <= ord(x) <= 1103, mark))
        if len(a) != len(mark):
            raise ValidateFormatStrError('Параметр "Марка Авто" должен содержать только символы кириллицы')
        return mark.capitalize()

    @staticmethod
    def __validate_model(model: str) -> str:
        """Метод для проверки введенной информации в Параметр "Модель авто" проверяется на пустое значение,
            проверка на тип вводимых данных (строка), а так же на вводимые символы"""

        if not isinstance(model, str):
            raise ValidateStrError('Параметр "Модель авто" должен быть строкой')
        if not model:
            raise EmptyNameError('Параметр "Модель авто" не может быть пустым')
        q = list(filter(lambda x: 48 <= ord(x) <= 1103, model))
        if len(q) != len(model):
            raise ValidateFormatStrError('Параметр "Модель авто" должен содержать только символы кириллицы и английский алфавит')
        return model.capitalize()

    @staticmethod
    def __validate_year_of_production(year_of_production: int) -> int:
        """Метод для проверки введенной информации в поле year_of_production, проверяется на пустое значение,
                     тип вводимых данных (целое число), а так же на верный диапазон года выпуска авто"""

        if not year_of_production:
            raise EmptyNameError('Параметр "Год выпуска" не может быть пустым')
        if not isinstance(year_of_production, int):
            raise ValidateIntError('Параметр "Год выпуска" должен быть целочисленным')
        if year_of_production < 2012 or year_of_production > 2024:
            raise ValidateFormatIntError('Параметр "Год выпуска" должен быть в диапазоне от 2012 до 2024')
        return year_of_production

    @staticmethod
    def __validate_color(color: str) -> str:
        """Метод для проверки введенной информации в поле color, проверяется на пустое значение,
                    проверка на тип вводимых данных (строка), а так же на вводимые символы"""

        if not isinstance(color, str):
            raise ValidateStrError('Параметр "Цвет авто" должен быть строкой')
        if not color:
            raise EmptyNameError('Параметр "Цвет авто" не может быть пустым')
        q = list(filter(lambda x: 1040 <= ord(x) <= 1103, color))
        if len(q) != len(color):
            raise ValidateFormatStrError('Параметр "Цвет авто" должен содержать только символы кириллицы')
        return color.capitalize()

    @staticmethod
    def __validate_price(price: float) -> float:
        """Метод для проверки введенной информации в параметр "Цена", проверяется на пустое значение,
                            проверка на тип вводимых данных (целочисленное значение)"""

        if not isinstance(price, float):
            raise ValidateFormatFloatError('Параметр "Цена" должен быть числом округленным до сотых')
        if not price:
            raise EmptyNameError('Параметр "Цена" не может быть пустым')
        return price

    @staticmethod
    def __validate_acceleration(acceleration: float) -> float:
        """Метод для проверки введенной информации в Параметр "Разгон до 100 км/ч,сек" проверяется на пустое значение,
                                    проверка на тип вводимых данных (число должно быть округлено до десятых)"""

        if not isinstance(acceleration, float):
            raise ValidateFormatFloatError('Параметр "Разгон до 100 км/ч,сек" должен быть числом округленным до десятых')
        if not acceleration:
            raise EmptyNameError('поле "Разгон до 100 км/ч,сек" не может быть пустым')
        return acceleration

    @staticmethod
    def __validate_equipment(equipment: dict) -> dict:
        """Метод для проверки введенной информации в поле equipment, проверяется на пустое значение,
        так же на вводимое значение ключа в формате str, а значение ключа"""

        #if equipment.items() not in equip_:
         #   raise EmptyNameError('поле equipment не может быть пустым')
        # q = list(filter(lambda x: 48 <= ord(x) <= 1103, equipment.values()))
        # if len(q) == len(equipment.values()):
        #     raise Exception('Параметр values(второй параметр) должен содержать только символы кириллицы, '
        #                     'цифры и английский алфавит')
        #return equipment

    @property
    def mark(self) -> str:
        return self.__mark

    @mark.setter
    def mark(self, mark):
        self.__mark = self.__validate_mark(mark)

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = self.__validate_model(model)

    @property
    def year_of_production(self) -> int:
        return self.__year_of_production

    @year_of_production.setter
    def year_of_production(self, year_of_production):
        self.__year_of_production = self.__validate_year_of_production(year_of_production)

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = self.__validate_color(color)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = self.__validate_price(price)

    @property
    def equipment(self) -> dict:
        return self.__equipment

    @equipment.setter
    def equipment(self, equipment, *args, **kwargs):
        equipment[args] = kwargs
        self.__equipment = self.__validate_equipment(equipment)

    @property
    def acceleration(self) -> float:
        return self.__acceleration

    @acceleration.setter
    def acceleration(self, acceleration):
        self.__acceleration = self.__validate_acceleration(acceleration)


car = Auto('huyndai', 'ix35', 2013, 'серый', 987554.20,
           {'Коробка передач': "automat", 'Электропакет': "full", 'Тип': "petrol",
            'Объем двигателя': 1.6, 'Производитель': 'Korea'}, 7.3)
print(car)
print(car.equipment)
car.equipment['Объем двигателя'] = 2.0
car.equipment['Тип'] = 'diesel'
print(car.equipment)


"""Задание 2.
Реализуйте класс «Точка в пространстве». Необходимо хранить в полях
класса: координату по оси X, координату по оси Y, координату по оси Z.
Реализуйте конструктор по умолчанию и метод для вывода данных объекта.
Реализуйте методы валидации данных для атрибутов объекта. Реализуйте
доступ к отдельным атрибутам класса через методы объекта (геттеры и
сеттеры), используя декоратор @property и @атрибут.setter."""


class Point_in_space:
    """Класс "Точка в пространстве"
     Класс описывает объект в виде точки в пространстве которая имеет свои координаты
     по трем осям, x, y, z, при помощи методов можно управлять положением точки в пространстве.
     методы позволяют менять ее координаты, а так же получать информацию о ее текущем местоположении
     Атрибуты:
        - designation - "Обозначение"
        - axis_x, axis_y, axis_z - оси x, y, z
    Класс в себе содержит следующие методы:
    - статик - методы(validate_атрибут) для валидации атрибутов
    - свойства атрибутов( @ property) для их вывода
    - сеттеры атрибутов( @ атрибут.setter) для изменения координат точки и изменения типа точки
     """

    def __init__(self, designation: str, axis_x: float, axis_y: float, axis_z: float):
        self.__designation = self.__validate_designation(designation)
        self.__axis_x = self.__validate_axis(axis_x)
        self.__axis_y = self.__validate_axis(axis_y)
        self.__axis_z = self.__validate_axis(axis_z)

    @staticmethod
    def __validate_designation(designation: str):
        """Метод для проверки введенной информации в поле name, проверяется на пустое значение,
                 проверка на тип вводимых данных (строка), а так же проверка на вводимые символы"""
        if not isinstance(designation, str):
            raise ValidateStrError('Параметр "обозначение"  должен быть строкой')
        if not designation:
            raise EmptyNameError('Параметр "обозначение" не может быть пустым')
        a = list(filter(lambda x: 48 <= ord(x) <= 1103, designation))
        if len(a) != len(designation):
            raise ValidateFormatStrError('Параметр "обозначение" может содержать символы кириллицы, цифры и английский алфавит')
        return designation.capitalize()

    @staticmethod
    def __validate_axis(axis: float) -> float:
        """Метод для проверки введенной информации в поле ось, проверяется на пустое значение,
                                проверка на тип вводимых данных (значение с плавающей точкой)"""
        if not isinstance(axis, float):
            raise ValidateIntError('Параметр "ось" должен быть числом округленным до десятых')
        if not axis:
            raise EmptyNameError('поле "ось" не может быть пустым')
        return axis


    def __str__(self):
        """Метод для вывода информации всех значений атрибутов на печать"""

        return (f'Название точки: {self.__designation} \n'
                f'Координата оси Х: {self.__axis_x}\n'
                f'Координата оси Y: {self.__axis_y}\n'
                f'Координата оси Z: {self.__axis_z}\n')

    @property
    def designation(self) -> str:
        return self.__designation

    @designation.setter
    def designation(self, designation: str):
        self.__designation = self.__validate_designation(designation)

    @property
    def axis_x(self) -> float:
        return self.__axis_x

    @axis_x.setter
    def axis_x(self, axis_x):
        self.__axis_x = self.__validate_axis(axis_x)

    @property
    def axis_y(self) -> float:
        return self.__axis_y

    @axis_y.setter
    def axis_y(self, axis_y):
        self.__axis_y = self.__validate_axis(axis_y)

    @property
    def axis_z(self) -> float:
        return self.__axis_z

    @axis_z.setter
    def axis_z(self, axis_z):
        self.__axis_z = self.__validate_axis(axis_z)


star = Point_in_space('sun', 1100.1, 245.9, 1186.7)
star.axis_x = 3000.8
print(star.axis_x)
star.axis_y = 5000.9
print(star.axis_y)
