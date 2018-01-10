#-*-coding:utf-8-*-
__author__ = 'loopsun'

from random import randint

class DataProvider(object):
    def __init__(self):
        pass

    def get_random_num_list(self, length=10, min=1, max=100):
        num_list = [randint(min, max) for i in range(length)]
        return num_list


def num_data_check(data):
    if data and isinstance(data, list):
        for i in data:
            if not isinstance(i, int):
                return False
        return True
    return False




if __name__ == '__main__':
    demo = DataProvider()
    print(demo.get_random_num_list())