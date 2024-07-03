"""Задание 1.
Реализуйте класс Retailltem (товарная единица), который содержит
данные о товаре в магазине. Этот класс должен хранить данные в атрибутах:
описание товара, количество единиц на складе и цена. После написания
этого класса напишите программу, которая создает три объекта Retailitem.
Создайте класс CashRegister (Кассовый аппарат), который может
использоваться вместе с классом Retailltem. Класс CashRegister должен иметь
внутренний список объектов Retailltem, а также приведенные ниже методы:
Метод purchase_item() (приобрести товар) в качестве аргумента
принимает объект Retailltem. При каждом вызове метода purchase_item()
объект Retailltem, передан­ный в качестве аргумента, должен быть добавлен в
список.
Метод get_total () (получить сумму покупки) возвращает общую
стоимость всех объектов Retailltem, хранящихся во внутреннем списке
объекта CashRegister.
Метод show_iterns () (показать товары) выводит данные об объектах
Retailltem, хранящихся во внутреннем списке объекта CashRegister.
Метод clear () (очистить) должен очистить внутренний список объекта
CashRegister.
Продемонстрируйте класс CashRegister в программе, которая
позволяет пользователю выбрать несколько товаров для покупки. Когда
пользователь готов рассчитаться за покупку, программа должна вывести
список всех товаров, которые он выбрал для покупки, а также их общую
стоимость."""

class RetailItem:

    def __init__(self, description: str, quantity: int, price: float):
        self._description = description
        self._quantity = quantity
        self._price = price

    def __str__(self):
        return (f'{self._description}; '
                f'Цена: {self._price}')

    def get_price(self):
        return self._price

def create_retail_item():
    item1 = RetailItem('Coca-cola', 10, 3.99)
    item2 = RetailItem('Burger', 8, 6.50)
    item3 = RetailItem('Potato-free', 12, 3.33)
    return [item1, item2, item3]


cola, burger, free = create_retail_item()

class CashRegister:
    _retail_item: [RetailItem] = []

    @staticmethod
    def purchase_item(item: [RetailItem]):
        CashRegister._retail_item.append(item)

    @staticmethod
    def get_item_price(item):
        price = RetailItem.get_price(item)
        return price

    @staticmethod
    def get_total():
        result = 0
        for i in CashRegister._retail_item:
            result += CashRegister.get_item_price(i)
        return f'Общая стоимость: {result}'

    @staticmethod
    def clear():
        return CashRegister._retail_item.clear()

    @staticmethod
    def show_items():
        print('В вашей корзине:')
        for i in CashRegister._retail_item:
            print(i)


def pay_client():
    register = CashRegister()
    register.purchase_item(cola)
    register.purchase_item(burger)
    register.purchase_item(free)
    CashRegister.clear()
    register.purchase_item(cola)
    register.purchase_item(burger)
    CashRegister.show_items()
    cash = CashRegister.get_total()
    print(cash)
    CashRegister.clear()

pay_client()
