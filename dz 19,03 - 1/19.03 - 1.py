"""Задание 1
Создайте класс Car, который будет содержать информацию об
автомобиле. С помощью механизма наследования, реализуйте класс
ElectricCar (содержит информацию об электроавтомобиле). Каждый из
классов должен содержать необходимые для работы методы. """
class Car:
    """
    Класс Авто описывает автомобиль.
    Атрибуты класса:
    - mark - Марка авто
    - year_of_production - год выпуска
    - color - цвет
    Методы:
        - свойства атрибутов (@property) для их вывода
        - сеттеры атрибутов (@атрибут.setter) для изменения значений атрибутов
    """

    def __init__(self, mark: str, year_of_production: int, color: str):
        self.__mark = mark
        self.__year_of_production = year_of_production
        self.__color = color

    def __str__(self):
        """Метод для вывода информации всех значений атрибутов на печать"""

        return (f'Марка Авто: {self.mark} \n'
                f'Год выпуска: {self.year_of_production}\n'
                f'Цвет кузова Авто: {self.color}\n')

    @property
    def mark(self) -> str:
        return self.__mark

    @mark.setter
    def mark(self, mark):
        self.__mark = mark

    @property
    def year_of_production(self) -> int:
        return self.__year_of_production

    @year_of_production.setter
    def year_of_production(self, year_of_production):
        self.__year_of_production = year_of_production

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

class ElectricCar(Car):
    def __init__(self, mark: str, year_of_production: int, color: str, battery_capacity: str):
        super().__init__(mark, year_of_production, color)
        self.__mark = mark
        self.__year_of_production = year_of_production
        self.__color = color
        self.__battery_capacity = battery_capacity

    @property
    def battery_capacity(self) -> str:
        return f'{self.__battery_capacity} AH'

    @battery_capacity.setter
    def battery_capacity(self, battery_capacity):
        self.__battery_capacity = battery_capacity


electorcar = ElectricCar('Tesla', 2012, 'black', 10000)
car = Car('Huyndai', 2013, 'Cерый')
print(car)
print(electorcar.year_of_production)
print(electorcar.battery_capacity)
