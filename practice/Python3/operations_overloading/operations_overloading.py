class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # unary operators
    def __invert__(self):
        self.x, self.y = self.y, self.x

    # binary operators
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __lt__(self, other):
        return self.x < other.x and self.y < self.y

    def __gt__(self, other):
        return self.x > other.x and self.y > self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == self.y

    def __ne__(self, other):
        return self.x != other.x and self.y != self.y

    def __xor__(self, pow):
        self.x = self.x ** pow
        self.y = self.y ** pow
        return self

p1 = Point(1, 3)
~p1
print(p1.x, p1.y)

p2 = Point(2, 2)
p3 = p1 + p2
print(p3.x, p3.y)

print(p1 > p2)
print(p1 < p2)
print(p1 == p2)
print(p1 != p2)

p1 = p1 ^ 3
print(p1.x, p1.y)
