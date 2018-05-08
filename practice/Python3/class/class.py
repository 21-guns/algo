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
