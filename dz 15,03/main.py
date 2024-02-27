"""Задание 1
    Создайте класс для конвертирования температуры из градусов
    Цельсия в градусы Фаренгейта, Кельвина и наоборот. У класса должно быть
    несколько статических методов"""
from Errors import ValidateFormatFloatError
class ConverterTemp:
    temp_F = 0
    temp_K = 0

    def __init__(self, name: str, temp_C: float):
        self.__name = name
        self.__temp_C = self.validate_temp_C(temp_C)


    @staticmethod
    def validate_temp_C(temp_C):
        if temp_C < -273.5:
            raise ValidateFormatFloatError('Температура не может быть ниже -273.5 градуса Цельсия')
        return temp_C
    @property
    def temp_C(self):
        return self.__temp_C
    @staticmethod
    def convertingIn_F(temp_C: float):
        temp_F = temp_C * 1.8 + 32
        return float(temp_F)

    @temp_C.setter
    def temp_C(self, temp_C):
        self.__temp_C = self.validate_temp_C(temp_C)


temp1 = ConverterTemp('Home', 22.5)

print(temp1.convertingIn_F(100))
temp1.temp_C = -273.0
print(temp1.convertingIn_F(100))
