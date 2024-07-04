import random

a = [random.randint(0, 100) for i in range(10)]
print(f'{a} основной массив')
def find_count(a: list):
    k, z = 0, 0
    for i in range(len(a)):
        if a[i] == 0:
            print(f'Для числа {a[i]} нужно одно действие до единицы')
            i += 1
        elif a[i] == 1:
            print(f'Число {a[i]} уже является единицей')
            i += 1
        elif a[i] == 2:
             print(f'Для числа  {a[i]} нужно одно действие до единицы')
             i += 1
        elif a[i] > 2:
            if a[i]%2 ==0:
                m = a[i]
                while m > 2:
                    if m % 2 == 1:
                        m += 1
                        z += 1
                    else:
                        m = int(m / 2)
                        z += 1
                        if m == 2:
                            print(f'Для числа  {int(a[i])} нужно {z+1} действия до единицы')
                            z = 0
                            i += 1
            else:
                m = a[i]
                while m > 2:
                    if m % 2 == 1:
                        m += 1
                        z += 1
                    else:
                        m = int(m / 2)
                        z += 1
                        if m == 2:
                            print(f'Для числа  {int(a[i])} нужно {z+1} действия до единицы')
                            z = 0
                            i += 1

find_count(a)
