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
        """Метод для проверки введенной информации в поле mark, проверяется на пустое значение,
            присутсвие цифр, проверка на тип вводимых данных (строка), а так же на вводимые символы"""

        if not mark:
            raise EmptyNameError('поле "Марка Авто" не может быть пустым')
        if mark.isdigit():
            raise ValidateFormatStrError('В поле "Марка Авто" не может быть цифр')
        a = list(filter(lambda x: 48 <= ord(x) <= 1103, mark))
        if len(a) != len(mark):
            raise ValidateFormatStrError('Параметр name должен содержать только символы кириллицы')
        if not isinstance(mark, str):
            raise ValidateStrError('Параметр name должен быть строкой')
        return mark.capitalize()

    @staticmethod
    def __validate_model(model: str) -> str:
        """Метод для проверки введенной информации в поле model, проверяется на пустое значение,
            проверка на тип вводимых данных (строка), а так же на вводимые символы"""

        if not model:
            raise EmptyNameError('поле "Модель Авто" не может быть пустым')
        q = list(filter(lambda x: 48 <= ord(x) <= 1103, model))
        if len(q) != len(model):
            raise ValidateFormatStrError('Параметр model должен содержать только символы кириллицы')
        if not isinstance(model, str):
            raise ValidateStrError('Параметр model должен быть строкой')
        return model.capitalize()

    @staticmethod
    def __validate_year_of_production(year_of_production: int) -> int:
        """Метод для проверки введенной информации в поле year_of_production, проверяется на пустое значение,
                     тип вводимых данных (целое число), а так же на верный диапазон года выпуска авто"""

        if not year_of_production:
            raise EmptyNameError('поле "Год выпуска" не может быть пустым')
        if not isinstance(year_of_production, int):
            raise ValidateIntError('Параметр Год выпуска должен быть целочисленным')
        if year_of_production < 2012 or year_of_production > 2024:
            raise ValidateFormatIntError('Параметр year_of_production должен быть в диапазоне от 2012 до 2024')
        return year_of_production

    @staticmethod
    def __validate_color(color: str) -> str:
        """Метод для проверки введенной информации в поле color, проверяется на пустое значение,
                    проверка на тип вводимых данных (строка), а так же на вводимые символы"""

        if not color:
            raise EmptyNameError('поле "цвет Авто" не может быть пустым')
        q = list(filter(lambda x: 1040 <= ord(x) <= 1103, color))
        if len(q) != len(color):
            raise ValidateFormatStrError('Параметр color должен содержать только символы кириллицы')
        if not isinstance(color, str):
            raise ValidateStrError('Параметр color должен быть строкой')
        return color.capitalize()

    @staticmethod
    def __validate_price(price: float) -> float:
        """Метод для проверки введенной информации в поле price, проверяется на пустое значение,
                            проверка на тип вводимых данных (целочисленное значение)"""

        if not price:
            raise EmptyNameError('поле price не может быть пустым')
        if not isinstance(price, float):
            raise ValidateFormatFloatError('Параметр price должен быть числом округленным до сотых')
        return price

    @staticmethod
    def __validate_acceleration(acceleration: float) -> float:
        """Метод для проверки введенной информации в поле acceleration, проверяется на пустое значение,
                                    проверка на тип вводимых данных (число должно быть округлено до десятых)"""

        if not acceleration:
            raise EmptyNameError('поле "Разгон до 100 км/ч,сек" не может быть пустым')
        if not isinstance(acceleration, float):
            raise ValidateFormatFloatError('Параметр "Разгон до 100 км/ч,сек" должен быть числом округленным до десятых')
        return acceleration

    @staticmethod
    def __validate_equipment(equipment: dict) -> dict:
        """Метод для проверки введенной информации в поле equipment, проверяется на пустое значение,
        так же на вводимое значение ключа в формате str, а значение ключа"""

        if not equipment:
            raise EmptyNameError('поле equipment не может быть пустым')
        # q = list(filter(lambda x: 48 <= ord(x) <= 1103, equipment.values()))
        # if len(q) == len(equipment.values()):
        #     raise Exception('Параметр values(второй параметр) должен содержать только символы кириллицы, '
        #                     'цифры и английский алфавит')
        return equipment

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
     методы позволяют менять ее координаты, а так же получать иформацию о ее текущем местоположении
    Класс в себе содержит следующие методы:
    - статик - методы(validate_атрибут) для валидации атрибутов
    - свойства атрибутов( @ property) для их вывода
    - сеттеры атрибутов( @ атрибут.setter) для изменеия координат точки и изменения типа точки
      True - истинная, False - Мнимая  """

    def __init__(self, designation: str, axis_x: float, axis_y: float, axis_z: float, point_type: bool):
        self.__designation = self.__validate_designation(designation)
        self.__axis_x = self.__validate_axis_x(axis_x)
        self.__axis_y = self.__validate_axis_y(axis_y)
        self.__axis_z = self.__validate_axis_z(axis_z)
        self.__point_type = self.__validate_point_type(point_type)

    @staticmethod
    def __validate_designation(designation: str):
        """Метод для проверки введенной информации в поле name, проверяется на пустое значение,
                 проверка на тип вводимых данных (строка), а так же проверка на вводимые символы"""
        if not designation:
            raise EmptyNameError('поле designation не может быть пустым')
        a = list(filter(lambda x: 48 <= ord(x) <= 1103, designation))
        if len(a) != len(designation):
            raise ValidateFormatStrError('Параметр designation может содержать символы кириллицы, цифры и английский алфавит')
        if not isinstance(designation, str):
            raise ValidateStrError('Параметр designation должен быть строкой')
        return designation.capitalize()

    @staticmethod
    def __validate_axis_x(axis_x: float) -> float:
        """Метод для проверки введенной информации в поле axis_x, проверяется на пустое значение,
                                проверка на тип вводимых данных (значение с плавающей точкой)"""

        if not axis_x:
            raise EmptyNameError('поле "ось х" не может быть пустым')
        if not isinstance(axis_x, float):
            raise ValidateIntError('Параметр axis_x должен быть числом')
        return axis_x

    @staticmethod
    def __validate_axis_y(axis_y: float) -> float:
        """Метод для проверки введенной информации в поле axis_y, проверяется на пустое значение,
                                проверка на тип вводимых данных (значение с плавающей точкой)"""

        if not axis_y:
            raise EmptyNameError('поле "ось y" не может быть пустым')
        if not isinstance(axis_y, float):
            raise ValidateIntError('Параметр axis_y должен быть числом')
        return axis_y

    @staticmethod
    def __validate_axis_z(axis_z: float) -> float:
        """Метод для проверки введенной информации в поле axis_z, проверяется на пустое значение,
                                проверка на тип вводимых данных (значение с плавающей точкой)"""

        if not axis_z:
            raise EmptyNameError('поле "ось z" не может быть пустым')
        if not isinstance(axis_z, float):
            raise ValidateIntError('Параметр axis_z должен быть числом')
        return axis_z

    @staticmethod
    def __validate_point_type(point_type: bool) -> bool:
        """Метод для проверки введенной информации в поле point_type,
                проверка на тип вводимых данных (значение True или False)"""
        if not isinstance(point_type, bool):
            raise ValidateFormatBoolError('Параметр point_type должен быть True или False')
        return point_type

    def __str__(self):
        """Метод для вывода информации всех значений атрибутов на печать"""

        return (f'Название точки: {self.__designation} \n'
                f'Координата оси Х: {self.__axis_x}\n'
                f'Координата оси Y: {self.__axis_y}\n'
                f'Координата оси Z: {self.__axis_z}\n'
                f'Тип точки: {self.__point_type}')

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
        self.__axis_x = self.__validate_axis_x(axis_x)

    @property
    def axis_y(self) -> float:
        return self.__axis_y

    @axis_y.setter
    def axis_y(self, axis_y):
        self.__axis_y = self.__validate_axis_y(axis_y)

    @property
    def axis_z(self) -> float:
        return self.__axis_z

    @axis_z.setter
    def axis_z(self, axis_z):
        self.__axis_z = self.__validate_axis_z(axis_z)

    @property
    def point_type(self) -> bool:
        return self.__point_type

    @point_type.setter
    def point_type(self, point_type):
        self.__point_type = self.__validate_point_type(point_type)


star = Point_in_space('sun', 1100.1, 245.9, 1186.7, True)
print(star.designation)
print(star)
star.point_type = False
print(star.axis_x)
star.axis_y = 1345.0
print(star)
