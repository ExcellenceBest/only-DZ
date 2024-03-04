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
        - перевод из Фаренгейта в Кельвин - converting_in_K_from_F
        """

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



"""Задание 2.  Создайте класс для перевода длинны из метрической в
имперскую(английскую) систему. У класса должно быть несколько статических методов"""

class Length_converter:
    """Класс создан для конвертации длины из системы СИ в английскую систему и наоборот.
    Атрибуты класса - length (число для конвертации)
    Методы класса:
        - convert_cm_in_inch перевод из см в дюймы
        - convert_inch_in_cm перевод из дюймов в см
        - convert_metre_in_foot перевод из метров в футы
        - convert_foot_in_metre перевод из футов в метры
        - convert_metre_in_yard перевод из метров в ярды
        - convert_yard_in_metre перевод из ярдов в метры
        - convert_kilometre_in_mile перевод из километров в мили
        - convert_mile_in_kilometre перевод из миль в километры
        """
    def __init__(self, length: float):

        self.length = length
    @staticmethod
    def convert_cm_in_inch(length: float):
        result = length / 2.54
        return f'{length} cм -> {round(result, 2)} дюйма'

    @staticmethod
    def convert_inch_in_cm(length: float):
        result = length * 2.54
        return f'{length} дюймов -> {round(result, 2)} см'

    @staticmethod
    def convert_metre_in_foot(length: float):
        result = length / 0.3048
        return f'{length} м -> {round(result, 2)} Футов'

    @staticmethod
    def convert_foot_in_metre(length: float):
        result = length * 0.3048
        return f'{length} Футов -> {round(result, 2)} М'

    @staticmethod
    def convert_metre_in_yard(length: float):
        result = length / 0.9144
        return f'{length} м -> {round(result, 2)} Ярдов'

    @staticmethod
    def convert_yard_in_metre(length: float):
        result = length * 0.9144
        return f'{length} Ярдов -> {round(result, 2)} М'


    @staticmethod
    def convert_kilometre_in_mile(length: float):
        result = length / 1.76
        return f'{length} км -> {round(result, 2)} Миль'

    @staticmethod
    def convert_mile_in_kilometre(length: float):
        result = length * 1.76
        return f'{length} Мили -> {round(result, 2)} км'

q = Length_converter(5)
print(q.convert_cm_in_inch(10))
print(q.convert_metre_in_foot(3))
print(q.convert_kilometre_in_mile(5))
print(q.convert_metre_in_yard(8))
print(q.convert_inch_in_cm(10))
print(q.convert_foot_in_metre(17))
print(q.convert_yard_in_metre(6))
print(q.convert_mile_in_kilometre(3))
