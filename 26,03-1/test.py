



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
print(bd)


def check_login(key: str):
    if key not in bd:
        print('Пользователь не зарегистрирован!')
    else:
        print('Пользователь зарегистрирован!')

def change_password(key: str, value: str):
    bd.update({key: value})
    print('Пароль успешно изменен!')

change_password('user', '1234')


       # raise ValueError('Новый пароль совпадает со старым')
# check('user3', '123455')
