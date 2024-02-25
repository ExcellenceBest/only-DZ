"""Задание 1. Реализуйте класс Автомобиль"""

class Auto:

    def __init__(self, mark: str, model: str, year_of_production: int, color: str, price: float, equipment: dict, acceleration: float):
        self.mark = self.__validate_mark(mark)
        self.model = model
        self.year_of_production = year_of_production
        self.color = color
        self.price = price
        self.equipment = equipment
        self.acceleration = acceleration

    def __str__(self):
        return (f'Марка Авто: {self.mark} \n'
                f'Модель Авто: {self.model}\n'
                f'Год выпуска: {self.year_of_production}\n'
                f'Цвет кузова Авто: {self.color}\n'
                f'Цена Авто: {self.price}\n'
                f'Комплектация Авто: {self.equipment}\n'
                f'Разгон до 100 км\ч,сек: {self.acceleration}')


    def __validate_mark(self, mark: str) -> str:
        if not mark:
            raise Exception('поле "Марка Авто" не может быть пустым')
        if mark.isdigit():
            raise Exception('В поле "Марка Авто" не может быть цифр')
        a = list(filter(lambda x: 1040 <= ord(x) <= 1103, mark))
        if len(a) != len(mark):
            raise Exception('Параметр name должен содержать только символы кириллицы')
        if not isinstance(mark, str):
            raise TypeError('Параметр name должен быть строкой')
        a = list(filter(lambda x: 1040 <= ord(x) <= 1103, mark))
        if len(a) != len(mark):
            raise Exception('Параметр name должен содержать только символы кириллицы')
        return mark.capitalize()




car = Auto("хендай33", 'ix35', 2013, 'grey',1300000,
           {'Коробка передач': "automat", 'Электропакет': "full", 'Тип': "petrol",
            'Объем двигателя': 2.0, 'Производитель': 'Korea'}, 7.8)
print(car)

