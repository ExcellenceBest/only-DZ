from abc import ABC, abstractmethod

"""Задание 1
Создайте базовый абстрактный класс ChessFigure. Опишите следующие
методы:
 Определить бьет ли она другую фигуру на поле
 Сделать ход на поле
 Определить возможность хода по правилам
 Определить текущие координаты
Создайте класс HorseFigure - наследника, класса ChessFigure и сделайте ход
на поле по правилам. """


class ChessFigure(ABC):

    @abstractmethod
    def move(self, coord):
        ...

    @abstractmethod
    def check_move(self, coord):
        ...

    @abstractmethod
    def get_coord(self):
        ...


class HorseFigure(ChessFigure):


    def __init__(self, column: str, row: str):
        self.column = self.validate_column(column)
        self.row = self.validate_row(row)

    @staticmethod
    def validate_column(column: str) -> str:
        if ord(column) < 65 or ord(column) > 72:
            raise ValueError("Буквенная координата выходит из диапазона А-Н")
        return column

    @staticmethod
    def validate_row(row: str) -> str:
        if int(row) < 1 or int(row) > 8:
            raise ValueError("Цифровая координата выходит за пределы 1-8")
        return row

    def get_coord(self) -> tuple:
        return self.column, self.row

    def check_move(self, coord: tuple) -> bool:
        x1 = ord(self.column) % 8
        y1 = int(self.row)

        if ord(coord[0]) < 65 or ord(coord[0]) > 72:
            raise ValueError("Буквенная координата выходит из диапазона А-Н")
        if int(coord[1]) < 1 or int(coord[1]) > 8:
            raise ValueError("Цифровая координата выходит за пределы 1-8")

        x2 = ord(coord[0]) % 8
        y2 = int(coord[1])


        x = abs(x2 - x1)
        y = abs(y2 - y1)

        return (x == 2 and y == 1) or (x == 1 and y == 2)

    def move(self, coord: tuple) -> bool:
        try:
            if self.check_move(coord):
               self.column, self.row = coord
            else:
                print(f"""Ход в {coord[0]}{coord[1]} невозможен""")
        except ValueError as e:
            print(f"""Ход в {coord[0]}{coord[1]} невозможен""")
        print(f'Ход выполнен!')

    def is_beats(self, coord: tuple) -> bool:

        x1 = ord(self.column) % 8
        y1 = int(self.row)

        x2 = ord(coord[0]) % 8
        y2 = int(coord[1])

        x = abs(x2 - x1)
        y = abs(y2 - y1)
        return (x == 2 and y == 1) or (x == 1 and y == 2)

horse1 = HorseFigure('E', '4')
horse2 = HorseFigure('D', '2')

def game(figure: HorseFigure):
    print(horse1.is_beats(horse2.get_coord()))
    horse1.move(('D', '6'))
    print(horse1.get_coord())

#game(horse1)

"""
Задание 2
Создайте базовый абстрактный класс SystemUser. Опишите следующие
методы:
 Информация о пользователе
 Вход в систему
 Выход из системы
 Сменить пароль
Создайте класс Employee - наследника, класса SystemUser и выполните вход
и выход в системе."""

class SystemUser(ABC):

    _status = False

    @abstractmethod
    def info(self):
        ...

    @abstractmethod
    def log_in(self):
        ...

    @abstractmethod
    def log_out(self):
        ...

    @abstractmethod
    def change_password(self, key: str, value: str, bd: dict):
        ...


class InitUser(SystemUser):

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    @staticmethod
    def create_bd(path: str):
        with open(path, 'r', encoding='utf-8') as file:
            bd1 = list(map(lambda x: x.rstrip('\n'), file.readlines()))
            result = {}
            for i in bd1:
                index = str.find(i, ',')
                fragment = i[(index + 1):]
                fragment1 = i[:index]
                result[fragment1] = fragment
        return result

    bd = create_bd('bd.txt')



    def check_login(self: SystemUser, bd=bd):
        key, value = self.info()
        if key not in bd:
             print('Пользователь не зарегистрирован!')
             return False
        else:
            print('Пользователь зарегистрирован!')
            return True


    def change_password(self: SystemUser, bd=bd):
        key, value = self.info()
        if bd.keys() == value:
            return False
            print('Пароль совпадает с предыдущим!')
        else:
            return bd.update({key: value})


class Employee(SystemUser):

    def __init__(self, login: str, password: str):
        self._login = login
        self._password = password

    def info(self):
        return self._login, self._password


    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password


    def change_password(self: SystemUser):
        if InitUser.change_password(self):
            print('Пароль успешно изменен!')
        else:
            print('Пароль совпадает с предыдущим!')





    def log_in(self: SystemUser):
        if InitUser.check_login(self):
            if not self._status:
                self._status = True
                print('Вы вошли в систему!')
            else:
                print('Пользователь в сети!')
        else:
            print("Пользователь отсутствует, требуется регистрация!")


    def log_out(self):
        if self._status:
            self._status = False
            print('Вы вышли из системы!')
        else:
            print('Пользователь не в сети!')

    @login.setter
    def login(self, login):
        self._login = login

    @password.setter
    def password(self, password):
        self._password = password


user1 = Employee('admin', '123456')
admin2 = Employee('admin2', '55555')
print(InitUser.create_bd('bd.txt'))
#user1.log_in()

user1.change_password('12121')


# def logging(user: SystemUser):
#     user.log_in()
#
# logging(user1)
