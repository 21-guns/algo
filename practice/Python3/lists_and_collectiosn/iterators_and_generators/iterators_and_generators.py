# reverse generator


def reverse(data):
    current = len(data)
    while current >= 1:
        current -= 1
        yield data[current]


for c in reverse("string"):
    print(c)

for i in reverse([1, 2, 3]):
    print(i)


# reverse iterator

class Reverse(object):
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


for c in Reverse("string"):
    print(c)

for i in Reverse([1, 2, 3]):
    print(i)


# simple generator
def counter(low, high, step):
    current = low
    while current <= high:
        yield current
        current += step


for c in counter(3, 9, 2):
    print(c)


# simple iterator

class Counter(object):
    def __init__(self, low, high, step):
        self.current = low
        self.high = high
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            result = self.current
            self.current += self.step
            return result


for c in Counter(3, 9, 2):
    print(c)
