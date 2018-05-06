from math import *

exclude_methods = frozenset(["__module__", "__qualname__"])


def class_extend(cls):
    class Meta(type):
        def __new__(self, name, bases, attrs, **kwargs):
            for name, value in attrs.items():
                if name not in exclude_methods:
                    setattr(cls, name, value)
                return cls

    return Meta


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point(metaclass=class_extend(Point)):
    def distance_to(self, p2):
        d1 = pow(self.x - p2.x, 2)
        d2 = pow(self.y - p2.y, 2)
        return sqrt(d1 + d2)

p1 = Point(1, 2)
p2 = Point(2, 3)

distance = p1.distance_to(p2)