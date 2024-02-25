"""Задание 1. Реализуйте класс Автомобиль"""


class Auto:
    """
    Класс Авто содержит атрибуты описывающие автомобили, его цвета, марки, модели, характеристики
    год выпуска, цена и время разгона до 100 км.ч
     mark, model, year_of_production, color, price, equipment, acceleration.
    Класс в себе содержит следующие методы:
        -методы для валидации атрибутов
        - Validate_атрибут - статик метод
        - свойства атрибутов @property) для их вывода
        - сеттеры атрибутов (@атрибут.setter) для изменеия значений атрибутов
    """
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
        """Метод для вывода инвормации всех значений атрибутов на печать"""

        return (f'Марка Авто: {self.mark} \n'
                f'Модель Авто: {self.model}\n'
                f'Год выпуска: {self.year_of_production}\n'
                f'Цвет кузова Авто: {self.color}\n'
                f'Цена Авто: {self.price}\n'
                f'Комплектация Авто: {self.equipment}\n'
                f'Разгон до 100 км\ч,сек: {self.acceleration}')


    @staticmethod
    def __validate_mark(mark: str) -> str:
        """Метод для проверки введенной информации в поле mark, проверяется на пустое значение,
            присутсвие цифр, проверка на тип вводимых данных (строка), а так же на вводимые символы"""

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
        """Метод для проверки введенной информации в поле model, проверяется на пустое значение,
            проверка на тип вводимых данных (строка), а так же на вводимые символы"""

        if not model:
            raise Exception('поле "Модель Авто" не может быть пустым')
        q = list(filter(lambda x: 48 <= ord(x) <= 1103, model))
        if len(q) != len(model):
            raise Exception('Параметр model должен содержать только символы кириллицы')
        if not isinstance(model, str):
            raise TypeError('Параметр model должен быть строкой')
        return model.capitalize()

    @staticmethod
    def __validate_year_of_production(year_of_production: int) -> int:
        """Метод для проверки введенной информации в поле year_of_production, проверяется на пустое значение,
                     тип вводимых данных (целое число)б а так же на верный диапазон года выпуска авто"""

        if not year_of_production:
            raise Exception('поле "Год выпуска" не может быть пустым')
        if not isinstance(year_of_production, int):
            raise TypeError('Параметр Год выпуска должен быть целочисленным')
        if year_of_production < 2012 or year_of_production > 2024:
            raise ValueError('Параметр year_of_production должен быть в диапазоне от 2012 до 2024')
        return year_of_production

    @staticmethod
    def __validate_color(color: str) -> str:
        """Метод для проверки введенной информации в поле color, проверяется на пустое значение,
                    проверка на тип вводимых данных (строка), а так же на вводимые символы"""

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
        """Метод для проверки введенной информации в поле price, проверяется на пустое значение,
                            проверка на тип вводимых данных (целочисленное значение)"""

        if not price:
            raise Exception('поле "Цена Авто" не может быть пустым')
        if not isinstance(price, int):
            raise TypeError('Параметр Цена должен быть числом')
        return price

    @staticmethod
    def __validate_acceleration(acceleration: float) -> float:
        """Метод для проверки введенной информации в поле acceleration, проверяется на пустое значение,
                                    проверка на тип вводимых данных (float, число с плавающей точкой)"""

        if not acceleration:
            raise Exception('поле "Разгон до 100 км\ч,сек" не может быть пустым')
        if not isinstance(acceleration, float):
            raise TypeError('Параметр "Разгон до 100 км\ч,сек" должен быть числом округленным до десятых')
        return acceleration

    @staticmethod
    def __validate_equipment(equipment: dict) -> dict:
        """Метод для проверки введенной информации в поле equipment, проверяется на пустое значение"""

        if not equipment:
            raise Exception('поле "Комплектация" не может быть пустым')
        #if not isinstance(equipment.keys() or equipment.values(), str or int or float):
         #   raise TypeError('Параметр  должен быть строкой')  в разработке
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
