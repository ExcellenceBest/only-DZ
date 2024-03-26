"""Используя механизм множественного наследования разработайте класс
«Легковой автомобиль». Создайте несколько классов-наследников согласно
примерной классификации. Создайте классы миксины «EngineMixIn»
(двигатель) и «TrailerMixIn» (прицеп). Используя классы-миксины
«примешайте» к классам наследникам несколько методов:
1. Метод класса TrailerMixIn, который добавляет груз в прицеп,
учитывая максимальную вместимость прицепа.
2. Метод класса EngineMixin, который заводит двигатель, учитывая
состояние двигателя «заведен» / «не заведен»."""


class PassengerCar:
    def __init__(self, title: str):
        self.title = title


class EngineMixIn:
    _engine_status = False

    @classmethod
    def start_engine(cls):
        if not cls._engine_status:
            cls._engine_status = True
            print("Двигатель заведен!")
        else:
            print("Двигатель уже заведен!")

class TrailerMixIn:
    _loaded = 0

    @classmethod
    def loading_cargo(cls, cargo: int, max_capacity: int = 750):
        if cargo + cls._loaded > max_capacity:
            raise ValueError("Перегруз!")
        else:
           cls._loaded += cargo
           print(f"загружено {cls._loaded} кг, доступно {max_capacity - cargo}кг для загрузки")


class ElectricCar(PassengerCar, EngineMixIn, TrailerMixIn):
    def __init__(self, title: str, battery_capacity: int):
        PassengerCar.__init__(self, title)
        TrailerMixIn.__init__(self)
        self.battery_capacity = battery_capacity


class RacingCar(PassengerCar, EngineMixIn, TrailerMixIn):
    def __init__(self, title: str, n2o_capacity: int):
        PassengerCar.__init__(self, title)
        self.n2o_capacity = n2o_capacity

car1 = ElectricCar('Tesla', 50000)
car2 = RacingCar('Lamba', 200)

def test(car):
    car.start_engine()
    car.start_engine()
    car.loading_cargo(100)

test(car1)
test(car2)
