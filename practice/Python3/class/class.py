# create a class and copy
import copy


class Shape(object):
    def __init__(self, line_count, name):
        self.line_count = line_count
        self.name = name


square = Shape(4, "Square")
square_copy = copy.deepcopy(square)


# nested class
class Shape(object):
    def __init__(self, line_count, name):
        self.line_count = line_count
        self.name = name

    class NestedClass(object):
        pass


square = Shape(4, "Square")
nested1 = square.NestedClass()


# define class
class SomeClass:
    pass


some_class = SomeClass()


# Read-only properties

## stored properties
class FilmList:
    def __init__(self):
        self.__count = 10

    @property
    def count(self):
        return self.__count


film_list = FilmList()
print(film_list.count)

## computed properties
import math


class Circle:
    def __init__(self, radius=0):
        self.__radius = radius

    @property
    def area(self):
        return 2 * math.pi * self.__radius


print(Circle(radius=10).area)


## stored properties
class Point:
    def __init__(self):
        self._x = 0
        self._y = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


point = Point()
point.x = 3
point.y = 7
print(point.x, point.y)

# lazy properties
from lazy import lazy


class FilmsList:
    def __init__(self):
        print("Some long operation")


class MediaPlayer:
    @lazy
    def films_list(self):
        return FilmsList()


player = MediaPlayer()
print("media player created")

film_list1 = player.films_list
film_list2 = player.films_list
print(film_list1 == film_list2)


## type properties

class ClassProperty(property):
    def __get__(self, instance, owner):
        return self.fget.__get__(None, owner)()


class Lesson:
    __lessonsCount = 0

    def __init__(self):
        Lesson.__lessonsCount += 1

    @classmethod
    def getCount(cls):
        return cls.__lessonsCount

    @classmethod
    def setCount(cls, value):
        cls.__lessonsCount = value

    lessonsCount = ClassProperty(getCount, setCount)


lesson1 = Lesson()
print(lesson1.lessonsCount)
lesson2 = Lesson()
print(lesson1.lessonsCount)


## in/out parameters

def swapStrings(s1, s2):
    s1[0], s2[0] = s2[0], s1[0]


s1 = ["A"]
s2 = ["B"]
swapStrings(s1, s2)

print(s1, s2)


## without any parameters
class Greeting:

    @classmethod
    def sayGoodbye(cls):
        print("GoodBye")

    @staticmethod
    def sayHello():
        print("Hello")

    def test(arg):
        print(arg)


Greeting.sayGoodbye()
Greeting.sayHello()
Greeting.test(1)


# array of parameters
def get_avg(*args):
    if len(args) == 0:
        return 0

    sum = 0
    for each in args:
        sum += each
    return sum / len(args)


print(get_avg(1, 2, 3, 4))


# variable parameters
def print5(data):
    if len(data) > 5:
        data = data[0: len(data) - 2]
    return data


print(1234567)



## replacement of the parent constructor
class Man:
    def __init__(self, name):
        self.name = name

class Position:
    def __init__(self, position):
        self.position = position


class Employee(Man, Position):
    def __del__(self):
        print("Died")

    def __enter__(self):
        print("Enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def __init__(self, name, position):
        super(Employee, self).__init__(name)
        Position.__init__(self, position)
        self.__private = "asdasfasgsaf"

    def __getitem__(self, item):
        pass


employee = Employee("Max", "teacher")
print(employee.name, employee.position)

