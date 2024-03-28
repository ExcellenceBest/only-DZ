"""Задание 1
    создайте класс для конвертирования температуры из градусов
    Цельсия в градусы Фаренгейта, Кельвина и наоборот. У класса должно быть
    несколько статических методов"""
from Errors import ValidateFormatFloatError


class ConverterTemp:
    """Класс описывает конвертирование температуры из градусов
    Цельсия в градусы Фаренгейта, Кельвина и наоборот.
    Methods :
        - метод валидации validate_temp
        - перевод из Цельсия в Фаренгейт - converting_in_F_from_C
        - перевод из Фаренгейта в Цельсий - converting_in_C_from_F
        - перевод из Цельсия в Кельвин - converting_in_K_from_C
        - перевод из Кельвина в Цельсий - converting_in_C_from_K """

    @staticmethod
    def validate_temp(__temp):
        if __temp < -273.5:
            raise ValidateFormatFloatError('Температура не может быть ниже -273.5 градуса Цельсия')
        return __temp

    @staticmethod
    def converting_in_F_from_C(temp_C: float):
        temp_F = temp_C * 1.8 + 32
        return temp_F

    @staticmethod
    def converting_in_C_from_K(temp_K: float):
        temp_C = temp_K - 273.15
        return temp_C

    @staticmethod
    def converting_in_C_from_F(temp_F: float):
        temp_C = (temp_F - 32) / 1.8
        return temp_C

    @staticmethod
    def converting_in_K_from_C(temp_C: float):
        temp_K = temp_C + 273.15
        return temp_K


print(ConverterTemp.converting_in_K_from_C(50))
print(ConverterTemp.converting_in_C_from_F(333))



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

    # FIXME: в этом классе конструктор не нужен, хоть один метод в классе задействует эти атрибуты?
    def __init__(self, length: float):

        self.length = length

    # FIXME: Метод должен вернуть значение, а не вывод, это обычный перевод одного значения в другое
    @staticmethod
    def convert_cm_in_inch(length: float):
        result = length / 2.54
        return f'{length} cм -> {round(result, 2)} дюйма'

    # FIXME: Метод должен вернуть значение, а не вывод, это обычный перевод одного значения в другое
    @staticmethod
    def convert_inch_in_cm(length: float):
        result = length * 2.54
        return f'{length} дюймов -> {round(result, 2)} см'

    # FIXME: Метод должен вернуть значение, а не вывод, это обычный перевод одного значения в другое
    @staticmethod
    def convert_metre_in_foot(length: float):
        result = length / 0.3048
        return f'{length} м -> {round(result, 2)} Футов'

    # FIXME: Метод должен вернуть значение, а не вывод, это обычный перевод одного значения в другое
    @staticmethod
    def convert_foot_in_metre(length: float):
        result = length * 0.3048
        return f'{length} Футов -> {round(result, 2)} М'

    # FIXME: Метод должен вернуть значение, а не вывод, это обычный перевод одного значения в другое
    @staticmethod
    def convert_metre_in_yard(length: float):
        result = length / 0.9144
        return f'{length} м -> {round(result, 2)} Ярдов'

    # FIXME: Метод должен вернуть значение, а не вывод, это обычный перевод одного значения в другое
    @staticmethod
    def convert_yard_in_metre(length: float):
        result = length * 0.9144
        return f'{length} Ярдов -> {round(result, 2)} М'

    # FIXME: Метод должен вернуть значение, а не вывод, это обычный перевод одного значения в другое
    @staticmethod
    def convert_kilometre_in_mile(length: float):
        result = length / 1.76
        return f'{length} км -> {round(result, 2)} Миль'

    # FIXME: Метод должен вернуть значение, а не вывод, это обычный перевод одного значения в другое
    @staticmethod
    def convert_mile_in_kilometre(length: float):
        result = length * 1.76
        return f'{length} Мили -> {round(result, 2)} км'

q = Length_converter(1)
print(q.convert_cm_in_inch(10))
print(q.convert_metre_in_foot(3))
print(q.convert_kilometre_in_mile(5))
print(q.convert_metre_in_yard(8))
print(q.convert_inch_in_cm(10))
print(q.convert_foot_in_metre(17))
print(q.convert_yard_in_metre(6))
print(q.convert_mile_in_kilometre(3))
