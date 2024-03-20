from  abc import ABC, abstractmethod
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

    _bd = {}
    path = 'bd.txt'

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    # @classmethod
    # def renew_bd(cls, _bd):
    #     return cls._bd == InitUser.read_bd(path)

    def __str__(self):
        return f' База:{self._bd}'

    @staticmethod
    def save_bd(_bd):
        new_bd = ''
        for k, v in _bd.items():
            new_bd += k + ',' + v + '\n'
        print(f' измененная база\n{new_bd}')
        bd3 = open('bd3', 'w', encoding='utf-8')
        bd3.write(new_bd)
        bd3.close()


    @staticmethod
    def read_bd(path: str, login=None, new_pass=None):
        with open(path, 'r', encoding='utf-8') as file:
            bd1 = list(map(lambda x: x.rstrip('\n'), file.readlines()))
            result = {}
            print(login)
            print(new_pass)
            for i in bd1:
                index = str.find(i, ',')
                log = i[:index]
                password = i[(index + 1):]
                if log == login:
                    result[log] = new_pass
                else:
                    result[log] = password
                print(result)
        return result


    def check_login(self):
        key, value = self.info()
        return False if key not in _bd else True

    def change_password(self, new_pass):
        (key, value) = self.info()
        return True if _bd[key] == new_pass else False

    def info(self):
        return self.login, self.password

    def login(self):
        return self.login

    def log_out(self):
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
            print('Вы в сети')
        else:
            print('Пользователь не зарегистрирован!\n'
                  'Желаете зарегистрироваться?')

    def log_out(self):
        ...

    def change_password(self, new_pass):
        if InitUser.change_password(self, new_pass):
            print('Пароль совпадает с предыдущим!')
        else:
            self._password = new_pass
            login = self._login
            InitUser.read_bd('bd.txt', login, new_pass)
            InitUser.save_bd(_bd)
            print('Пароль успешно изменен!')



_bd = InitUser.read_bd('bd.txt')

best_user = Employee('admin', 'week0497')
guest1 = Employee('user1', '1111')
guest2 = Employee('user2', '22222')
guest3 = Employee('user3', '333')

print(best_user.info())
# guest3.log_in()
best_user.change_password('12345')
print(best_user.info())
_bd = InitUser.read_bd('bd.txt',None, None)
print(_bd)
print(best_user.info())


# def check_login(key: str):
#     if key not in bd:
#         print('Пользователь не зарегистрирован!')
#     else:
#         print('Пользователь зарегистрирован!')
#
# def change_password(key: str, value: str):
#     bd.update({key: value})
#     print('Пароль успешно изменен!')
#
# change_password('user', '1234')
