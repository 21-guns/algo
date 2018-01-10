#-*-coding:utf-8-*-
__author__ = 'loopsun'

from sort.data import num_data_check, DataProvider

def insertion_sort(data):
    if num_data_check(data):
        print("排序前列表: ", data)
        sorted_index = 0
        for i in range(sorted_index + 1, len(data)):
            for k in range(sorted_index + 1):
                if data[i] < data[k]:
                    data.insert(k, data[i])
                    del data[i + 1]
            sorted_index += 1
        print("选择排序后列表: ", data)
        return data
    else:
        return data


if __name__ == '__main__':
    test_demo = DataProvider().get_random_num_list()
    insertion_sort(test_demo)
