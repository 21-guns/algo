# conformance checking
from abc import *


class PUID(ABC):
    id = 0


class Named(ABC):
    name = ""


class Flower(Named):
    def __init__(self, name):
        self.name = name


rose = Flower("Rose")
isPUID = isinstance(rose, PUID)
print(isPUID)
isNamed = isinstance(rose, Named)
print(isNamed)


# multi inheritance

class PID(ABC):
    @property
    @abstractmethod
    def id(self):
        pass


class Priced(ABC):
    @property
    @abstractmethod
    def price(self):
        pass


class Goods(PID, Priced):
    def __init__(self, id, price):
        self._id = id
        self._price = price

    @property
    def id(self):
        return self._id

    @property
    def price(self):
        return self._price


def show_id_and_price(info):
    print(info.id)
    print(info.price)


bread = Goods(1, 5)
show_id_and_price(bread)


# declaration and initialization
class Printable(ABC):
    @abstractmethod
    def print(self, color):
        pass


# properties requirements

class ACar(ABC):
    @property
    @abstractmethod
    def engine_volume(self):
        pass

    @engine_volume.setter
    @abstractmethod
    def engine_volume(self, val):
        pass


class AirWave(ACar):
    def __init__(self):
        self._engine_volume = 1500

    @property
    def engine_volume(self):
        return self._engine_volume

    @engine_volume.setter
    def engine_volume(self, val):
        self._engine_volume = val


airwave = AirWave()
print(airwave.engine_volume)
airwave.engine_volume = airwave.engine_volume * 1000
print(airwave.engine_volume)


# Inheritance of abstract classes
class AVehicle(ABC):
    @property
    @abstractmethod
    def max_speed(self):
        pass


class ATruck(AVehicle):
    @property
    @abstractmethod
    def capacity(self):
        pass


class Kamaz5320(ATruck):
    @property
    def max_speed(self):
        return 85

    @property
    def capacity(self):
        return 8000


kamaz = Kamaz5320()
max_speed = kamaz.max_speed
print(max_speed)


# collection of similar objects
class ANamed(ABC):
    name = ""


class Flower(ANamed):
    pass


class City(ANamed):
    pass


class Star(ANamed):
    pass


rose = Flower()
rose.name = "Rose"

rome = City()
rome.name = "Rome"

sirius = Star()
sirius.name = "Sirius"

rows = [rose, rome, sirius]
names = ",".join([r.name for r in rows])
print(names)


# method requirements

class Car(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class SportCar(Car):
    def __init__(self):
        self.started = False

    def start_engine(self):
        if self.started:
            return False
        else:
            self.started = True
        return True

    def stop_engine(self):
        if not self.started:
            return False
        else:
            self.started = False
        return True


sport_car = SportCar()
print(sport_car.start_engine())
print(sport_car.stop_engine())


# constructor requirements
class List(ABC):
    @abstractmethod
    def __init__(self, item_count):
        pass


class SortedList(List):
    def __init__(self, item_count):
        self._item_count = item_count
        print(self._item_count)


sorted_list = SortedList(10)


# subscript requirements

class AIterable(ABC):
    @abstractmethod
    def __getitem__(self, item):
        pass


class PowerOfTwo(AIterable):
    def __getitem__(self, item):
        return pow(2, item)


power = PowerOfTwo()
p8 = power[8]

p16 = power[16]

print(p8, p16)
