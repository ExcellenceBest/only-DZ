from abc import ABC, abstractmethod
"""Задание 1
Рассмотрим принцип разделения интерфейсов на следующем примере.
Допустим у нас имеется абстрактный класс Payments и в нем есть три метода:
оплата через электронный кошелек, оплата банковской карточкой и оплата
по QR коду.
Выполните разделение интерфейса и создайте два класса-наследника,
которые будут у себя реализовывать различные виды проведения оплат (класс
InternetPaymentService и TerminalPaymentService). При этом
TerminalPaymentService не должен поддерживать проведение оплат через
электронный кошелек."""

class Payments(ABC):

    @abstractmethod
    def pay_web_money(self):
        ...

    @abstractmethod
    def pay_credit_card(self):
        ...

    @abstractmethod
    def pay_qr_code(self):
        ...


class InternetPaymentService(Payments):

    def pay_web_money(self):
        print('Оплачено через WebMoney')


class TerminalPaymentService(Payments):

    def pay_web_money(self):
        raise ConnectionError('Оплата через сервис pay_web_money невозможна')


    def pay_credit_card(self):
        print("Оплачено кредитной картой")

    def pay_qr_code(self):
        print('Оплачено по QR коду')


"""Задание 2
Рассмотрим принцип инверсии зависимостей на следующем примере.
Исправьте код таким образом, чтобы классы и верхних, и нижних уровней
зависели от одних и тех же абстракций, а не от конкретных реализаций."""

class Authentication(ABC):
    def do_authentication(self):
        ...
class AnonymousAuthentication(Authentication):
    def do_authentication(self):
        ...

class GithubAuthentication(Authentication):
    def do_authentication(self):
        ...

class FacebookAuthentication(Authentication):
    def do_authentication(self):
        ...

class Permissions(AnonymousAuthentication):
    def __init__(self, auth: AnonymousAuthentication):
        self.auth = auth

    def getPermissions(self):
        self.auth.do_authentication()
