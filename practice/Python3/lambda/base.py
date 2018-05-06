from random import randint

x = 5
y = 6

# not recommend in PEP8, do not assign a lambda expression , use a def
addYToX = lambda x, y: x + y

print(addYToX(x, y))


# recommend in PEP8
def add_x_to_y():
    return lambda x, y: x + y


addYToXFunction = add_x_to_y()

print(addYToXFunction(x, y))

numbers = [randint(0, 10) for i in range(10)]

# lambda
numbers_1_1 = list(map(lambda x: x * 2 + 1, numbers))
numbers_1_2 = list(filter(lambda x: x % 3 == 0, numbers))
print(numbers_1_1)
print(numbers_1_2)


# define functions
def do_something(x):
    return x * 2 + 1


def do_another(x):
    return x % 3 == 0


numbers_2_1 = list(map(do_something, numbers))
numbers_2_2 = list(filter(do_another, numbers))

print(numbers_2_1)
print(numbers_2_2)


# capture of variables
def increment(n):
    return lambda x: x + n


inc_3 = increment(3)
inc_5 = increment(5)
print(inc_3(10))
print(inc_5(10))

# with a parameter

pow_of_two = lambda power: pow(2.0, power)
pow8 = pow_of_two(8)
print(pow8)


def pow_of_three(power):
    return pow(3.0, power)


pow8 = pow_of_three(8)
print(pow8)

# with multi parameter

avg = lambda a, b: (a + b) / 2
avg_1 = avg(4, 8)
print(avg_1)


def get_avg(a, b):
    return (a + b) / 2


avg_2 = get_avg(4, 8)
print(avg_2)

# with multi operators

from math import *


class point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_distances(p1, p2):
    d1 = pow(p1.x - p2.x, 2)
    d2 = pow(p1.y - p2.y, 2)
    return sqrt(d1 + d2)


point1 = point(0, 0)
point2 = point(5, 5)
distance = get_distances(point1, point2)
print(distance)


# currying
def carry(f):
    return lambda a: lambda b: f(a, b)


avg = lambda a, b: (a + b) / 2
n1 = avg(1, 2)
print(n1)

avg_1 = carry(avg)(1)
n2 = avg_1(3)
print(n2)

curried_avg = lambda a: lambda b: (a + b) / 2

avg3 = curried_avg(3)

n3 = avg3(3)
print(n3)

# return None
add_2_and_print = lambda a: print(a + 2)
print(add_2_and_print(10))


def add_3_and_print(a):
    print(a + 3)


print(add_3_and_print(10))


# Void function as parameter
def check_and_process(number, process):
    if number < 10:
        process(number)


check_and_process(5, lambda number: print(number * 10))
