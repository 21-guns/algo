# if no exception occurred
def throw_if_true(param):
    try:
        if param:
            raise Exception("test exception")
    except Exception as e:
        print("except")
    else:
        print("else")


throw_if_true(True)
throw_if_true(False)


# guaranteed code execution
def throw_if_true(param):
    try:
        if param:
            raise Exception("test exception")
    except Exception as e:
        print("except")
    finally:
        print("finally")


throw_if_true(True)
throw_if_true(False)


# define an exception type
class SimpleException(Exception):
    def __str__(self):
        return "SimpleException"


class RecommendExc(Exception):
    def __init__(self, arg):
        self.args = arg

# catch the specific exception
try:
    raise SimpleException()
except SimpleException as e:
    print(e.__str__())

try:
    raise RecommendExc("exception")
except RecommendExc as e:
    print(e.__str__())

# catch all exception
try:
    raise RecommendExc("exception")
except Exception as e:
    print(e.__str__())

# method throw an exception
def method_with_exception():
    raise Exception("Test")

# re-throw exceptions
try:
    method_with_exception()
except Exception as e:
    raise e