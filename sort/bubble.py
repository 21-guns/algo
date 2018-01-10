#-*-coding:utf-8-*-
__author__ = 'loopsun'
from sort.data import num_data_check, DataProvider

def bubble_sort(data):
    if num_data_check(data):
        print("排序前列表: ", data)
        while True:
            sortedTime = 0
            for i in range(len(data) - 1):
                if data[i] > data[i+1]:
                    data[i], data[i+1] = data[i+1], data[i]
                    sortedTime += 1
            if not sortedTime:
                break
        print("冒泡排序后列表: ", data)
        return data
    else:
        return data



if __name__ == '__main__':
    test_demo = DataProvider().get_random_num_list()
    bubble_sort(test_demo)