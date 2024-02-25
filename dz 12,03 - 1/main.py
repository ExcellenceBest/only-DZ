"""Задание 1. Реализуйте класс Автомобиль"""


class Auto:

    def __init__(self, mark: str, model: str, year_of_production: int, color: str, price: int, equipment: dict,
                 acceleration: float):
        self.__mark = self.__validate_mark(mark)
        self.__model = self.__validate_model(model)
        self.__year_of_production = self.__validate_year_of_production(year_of_production)
        self.__color = self.__validate_color(color)
        self.__price = self.__validate_price(price)
        self.__equipment = self.__validate_equipment(equipment)
        self.__acceleration = self.__validate_acceleration(acceleration)

    def __str__(self):
        return (f'Марка Авто: {self.mark} \n'
                f'Модель Авто: {self.model}\n'
                f'Год выпуска: {self.year_of_production}\n'
                f'Цвет кузова Авто: {self.color}\n'
                f'Цена Авто: {self.price}\n'
                f'Комплектация Авто: {self.equipment}\n'
                f'Разгон до 100 км\ч,сек: {self.acceleration}')

    @staticmethod
    def __validate_mark(mark: str) -> str:
        if not mark:
            raise Exception('поле "Марка Авто" не может быть пустым')
        if mark.isdigit():
            raise Exception('В поле "Марка Авто" не может быть цифр')
        a = list(filter(lambda x: 48 <= ord(x) <= 1103, mark))
        if len(a) != len(mark):
            raise Exception('Параметр name должен содержать только символы кириллицы')
        if not isinstance(mark, str):
            raise TypeError('Параметр name должен быть строкой')
        return mark.capitalize()

    @staticmethod
    def __validate_model(model: str) -> str:
        if not model:
            raise Exception('поле "Модель Авто" не может быть пустым')
        q = list(filter(lambda x: 48 <= ord(x) <= 1103, model))
        if len(q) != len(model):
            raise Exception('Параметр model должен содержать только символы кириллицы')
        if not isinstance(model, str):
            raise TypeError('Параметр model должен быть строкой')
        return model.capitalize()

    @staticmethod
    def __validate_year_of_production(year_of_production: int)-> int:
        if not year_of_production:
            raise Exception('поле "Год выпуска" не может быть пустым')
        if not isinstance(year_of_production, int):
            raise TypeError('Параметр Год выпуска должен быть целочисленным')
        return year_of_production

    @staticmethod
    def __validate_color(color: str) -> str:
        if not color:
            raise Exception('поле "цвет Авто" не может быть пустым')
        q = list(filter(lambda x: 1040 <= ord(x) <= 1103, color))
        if len(q) != len(color):
            raise Exception('Параметр color должен содержать только символы кириллицы')
        if not isinstance(color, str):
            raise TypeError('Параметр color должен быть строкой')
        return color.capitalize()

    @staticmethod
    def __validate_price(price: int) -> int:
        if not price:
            raise Exception('поле "Цена Авто" не может быть пустым')
        if not isinstance(price, int):
            raise TypeError('Параметр Цена должен быть числом')
        return price

    @staticmethod
    def __validate_acceleration(acceleration: float) -> float:
        if not acceleration:
            raise Exception('поле "Разгон до 100 км\ч,сек" не может быть пустым')
        if not isinstance(acceleration, float):
            raise TypeError('Параметр "Разгон до 100 км\ч,сек" должен быть числом округленным до десятых')
        return acceleration

    @staticmethod
    def __validate_equipment(equipment: dict) -> dict:
        if not equipment:
            raise Exception('поле "Комплектация" не может быть пустым')
        #if not isinstance(equipment.keys() or equipment.values(), str or int or float):
         #   raise TypeError('Параметр  должен быть строкой')
        return equipment

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        self.__mark = self.__validate_mark(mark)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = self.__validate_model(model)

    @property
    def year_of_production(self):
        return self.__year_of_production

    @year_of_production.setter
    def year_of_production(self, year_of_production):
        self.__year_of_production = self.__validate_year_of_production(year_of_production)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = self.__validate_color(color)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = self.__validate_price(price)

    @property
    def equipment(self):
        return self.__equipment

    @equipment.setter
    def equipment(self, equipment, *args, **kwargs):
        equipment[args] = kwargs
        self.__equipment = self.__validate_equipment(equipment)

    @property
    def acceleration(self):
        return self.__acceleration

    @acceleration.setter
    def acceleration(self, acceleration):
        self.__acceleration = self.__validate_acceleration(acceleration)



car = Auto("huyndai", 'IX35', 2013, 'серый', 1300000,
           {'Коробка передач': "automat", 'Электропакет': "full", 'Тип': "petrol",
            'Объем двигателя': 2.0, 'Производитель': 'Korea'}, 7.3)
print(car)
print(car.equipment)
car.equipment['Объем двигателя'] = 1.6
print(car.equipment)
