"""Задание 1
    создайте класс для конвертирования температуры из градусов
    Цельсия в градусы Фаренгейта, Кельвина и наоборот. У класса должно быть
    несколько статических методов"""
from Errors import ValidateFormatFloatError


class ConverterTemp:
    """Класс создан для перевода температуры из разных метрических систем
    в разные
    Атрибуты класса :
        - Имя (name) Объекта
        - Температура (temp) Объекта
    Класс содержит статические методы :
        - метод валидации validate_temp
        - перевод из Цельсия в Фаренгейт - converting_in_F_from_C
        - перевод из Кельвина в Фаренгейт - converting_in_F_from_K
        - перевод из Кельвина в Цельсий - converting_in_C_from_K
        - перевод из Фаренгейта в Цельсий - converting_in_C_from_F
        - перевод из Цельсия в Кельвин - converting_in_K_from_C
        - перевод из Фаренгейта в Кельвин - converting_in_K_from_F"""

    def __init__(self, name: str, temp: float):
        self.__name = name
        self.__temp = self.validate_temp(temp)



    @staticmethod
    def validate_temp(__temp):
        if __temp < -273.5:
            raise ValidateFormatFloatError('Температура не может быть ниже -273.5 градуса Цельсия')
        return __temp

    @staticmethod
    def converting_in_F_from_C(temp_C: float):
        temp_F = temp_C * 1.8 + 32
        return f'{round(float(temp_F),2)} по Фаренгейту'

    @staticmethod
    def converting_in_F_from_K(temp_K: float):
        temp_F = temp_K * 9/5 - 459.67
        return f'{round(float(temp_F),2)} по Фаренгейту'

    @staticmethod
    def converting_in_C_from_K(temp_K: float):
        temp_C = temp_K - 273.15
        return f'{round(float(temp_C), 2)} по Цельсию'

    @staticmethod
    def converting_in_C_from_F(temp_F: float):
        temp_C = (temp_F - 32) / 1.8
        return f'{round(float(temp_C), 2)} по Цельсию'

    @staticmethod
    def converting_in_K_from_C(temp_C: float):
        temp_K = temp_C + 273.15
        return f'{float(temp_K)} по Кельвину'

    @staticmethod
    def converting_in_K_from_F(temp_F: float):
        temp_K = (temp_F + 459.67) * 5/9
        return f'{round(float(temp_K),2)} по Кельвину'


a = ConverterTemp('body', 36.6)
print(a.converting_in_K_from_C(50))
print(a.converting_in_F_from_K(60))
print(a.converting_in_F_from_K(300))
print(a.converting_in_C_from_F(333))




# """Задание 2.  Создайте класс для перевода длинны из метрической в
# имперскую(английскую) систему. У класса должно быть несколько статических методов
# Дюйм (inch) = 25,4 мм (2,54 см)
# Фут (foot) = 0,3048 м (или 12 дюймов)
# Ярд (yard) = 0,9144 м (или 3 фута)
# Миля (mile) = 1,609 км (или 1,760 ярда)"""
#
