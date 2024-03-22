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

game(horse1)

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

from abc import ABC, abstractmethod


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
    def change_password(self, new_pass):
        ...


class InitUser(SystemUser):

    path = 'bd.txt'

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    @staticmethod
    def init_bd(login, new_pass):
        with open(InitUser.path, 'r', encoding='utf-8') as file:
            bd1 = list(map(lambda x: x.rstrip('\n'), file.readlines()))
            result = {}
            new_bd = ''
            if not bd1:
                result[login] = new_pass
            for i in bd1:
                index = str.find(i, ',')
                log = i[:index]
                password = i[(index + 1):]
                if log == login:
                    result[log] = new_pass
                else:
                    result[log] = password
            if login not in result:
                result[login] = password
            for k, v in result.items():
                new_bd += k + ',' + v + '\n'
            bd3 = open('bd.txt', 'w', encoding='utf-8')
            bd3.write(new_bd)
            bd3.close()
        return result

    def check_login(self):
        key, value = self.info()
        return False if key not in _bd else True

    def change_password(self, new_pass):
        (key, value) = self.info()
        return True if _bd[key] == new_pass else False

    @staticmethod
    def registration(login, password):
        InitUser.init_bd(login, password)

    def info(self):
        return self.login, self.password

    def login(self):
        return self.login

    def log_out(self):
        ...

    def log_in(self):
        ...


class Employee(SystemUser):

    def __init__(self, login: str, password: str):
        self._login = login
        self._password = password

    def info(self):
        return self._login, self._password

    def login(self):
        return self._login

    def log_in(self):
        if InitUser.check_login(self):
            print(f'{self._login} Вы в сети')
            _status = True
        else:
            print('Пользователь не зарегистрирован!\n'
                  'Желаете зарегистрироваться?')

    def log_out(self):
        _status = False
        print(f'{self._login} Вы вышли из сети!')

    def change_password(self, new_pass):
        if InitUser.change_password(self, new_pass):
            print('Пароль совпадает с предыдущим!')
        else:
            self._password = new_pass
            login = self._login
            InitUser.init_bd(login, new_pass)
            print(f'{self._login} Пароль успешно изменен!')

    @staticmethod
    def registration(login: str, password: str):
        InitUser.registration(login, password)
        print(f'{login} Вы зарегистрированы!')

_bd = InitUser.init_bd('admin', '00000')
best_user = Employee('admin', 'week0497')
guest1 = Employee('user1', '1111')
guest2 = Employee('user2', '22222')
guest3 = Employee('user3', '333')
guest1.registration('user1', '1111')
guest3.registration('user3', '333')
best_user.registration('admin', 'week0497')
best_user.change_password('dfhsathfd')
def logging(user: SystemUser):
    user.log_in()
    user.log_out()

logging(guest1)
logging(guest3)

