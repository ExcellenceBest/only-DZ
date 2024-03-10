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
                f'Цвет кузова Авто: {self.color}')

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
    def __init__(self, mark: str, year_of_production: int, color: str, battery_capacity: int):
        super().__init__(mark, year_of_production, color)
        self.__mark = mark
        self.__year_of_production = year_of_production
        self.__color = color
        self.__battery_capacity = battery_capacity

    @property
    def battery_capacity(self) -> str:
        return f'{self.__battery_capacity} AH\n'

    @battery_capacity.setter
    def battery_capacity(self, battery_capacity):
        self.__battery_capacity = battery_capacity


electric_car = ElectricCar('Tesla', 2012, 'black', 10000)
car = Car('Huyndai', 2013, 'Cерый')
print(car)
print(electric_car.year_of_production)
print(electric_car.battery_capacity)

"""Задание 2
Создайте класс Device, который будет содержать информацию об
электронном устройстве. С помощью механизма наследования, реализуйте
класс MobilePhone (содержит информацию об мобильном телефоне). Каждый
из классов должен содержать необходимые для работы методы."""

class Device:
    def __init__(self, title: str, color: str, memory_capacity: int):
        self.__title = title
        self.__color = color
        self.__memory_capacity = memory_capacity

    def __str__(self):
        return (f'Название усройства {self.__title}\n'
                f'Цвет устройства {self.__color}\n'
                f'Объем памяти устройства {self.__memory_capacity}')

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def memory_capacity(self) -> int:
        return self.__memory_capacity

    @memory_capacity.setter
    def memory_capacity(self, memory_capacity):
        self.__memory_capacity = memory_capacity


class MobilePhone(Device):
    def __init__(self, title: str, color: str, memory_capacity: int,
                 battery_capacity: int, display_size: float):
        super().__init__(title, color, memory_capacity)
        self.__battery_capacity = battery_capacity
        self.__display_size = display_size

    @property
    def battery_capacity(self) -> int:
        return f'{self.__battery_capacity} mah'

    @battery_capacity.setter
    def battery_capacity(self, battery_capacity):
        self.__battery_capacity = battery_capacity

    @property
    def display_size(self) -> float:
        return f'{self.__display_size}"'

    @display_size.setter
    def display_size(self,display_size):
        self.__display_size = display_size


mobile1 = MobilePhone('Iphone', 'white', 16, 5000, 6.4)
print(mobile1)
print(mobile1.battery_capacity)
print(mobile1.display_size)

