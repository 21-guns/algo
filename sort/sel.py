#-*-coding:utf-8-*-
__author__ = 'loopsun'

from sort.data import num_data_check, DataProvider


def sel_sort(data):
    if num_data_check(data):
        print("排序前列表: ", data)
        new_data = []
        while len(data) > 1:
            init_index = 0
            min = data[init_index]
            for i in range(1, len(data)):
                if data[i] < min:
                    min = data[i]
                    init_index = i
            del data[init_index]
            new_data.append(min)
        new_data.extend(data)
        print("选择排序后列表: ", new_data)
        return new_data
    else:
        return data


if __name__ == '__main__':
    test_demo = DataProvider().get_random_num_list()
    sel_sort(test_demo)