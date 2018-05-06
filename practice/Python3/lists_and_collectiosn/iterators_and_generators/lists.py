# array length
numbers = [1, 2, 3]

length = len(numbers)
print(length)

# checking equality of arrays
n1 = [1, 2, 3]
n2 = [1, 2, 3]
n3 = [3, 2, 1]

print(n1 == n2)
print(n1 == n3)

# dynamic lists
count = 15
ar_int = [0] * count
ar_int[0] = 1
print(ar_int)

# get unique values
numbers = [1, 3, 2, 1, 3]
unique = list(set(numbers))

# list copy
numbers1 = [1, 2, 3, 4, 5]
numbers2 = list(numbers1)
numbers3 = numbers1[:]
import copy

numbers4 = copy.deepcopy(numbers1)
numbers1.append(6)
print(numbers1)
print(numbers2)
print(numbers3)
print(numbers4)

print(id(numbers1))
print(id(numbers2))
print(id(numbers3))
print(id(numbers4))

# filtering of elements
odd_items = [item for item in numbers1 if item % 2]
print(odd_items)


def get_odd(n):
    return n % 2


print(list(filter(get_odd, numbers1)))


# array with a default value
value = 5
count = 3

array = [value] * count
print(array)


# sorting of elements
numbers = [11, 2, 5, 7, 3]
numbers.sort()
print(numbers)
print(numbers.sort(reverse=True))

arr = [['B', 3], ['A', 2], ['C', 1]]
arr.sort(key=lambda x: x[0])
print(arr)
arr.sort(key=lambda x: x[0], reverse=True)
print(arr)


# arrays merging
numbers1 = [1]
numbers2 = [2]
numbers3 = numbers1 + numbers2
print(numbers3)

# list initialization
n1 = []
n2 = list()

n3 = [1, 2, 3]
n4 = ["1", "2", "3"]

n5 = [[1, 2], [3, 4, 5]]

# converting of array
numbers = [1, 2, 3, 4, 5]
numbers = [num * 3 for num in numbers]
print(numbers)

numbers = list(map(lambda x: x * 2, numbers))
print(numbers)

# checking of presence an element
numbers = [2, 3, 5, 7, 11, 13, 17]
print(5 in numbers)

print(numbers.index(5))

print(numbers.count(2))

# adding and removing of elements
numbers = [2, 5 ,7]
numbers.append(11)

print(numbers)
numbers.insert(1, 3)

print(numbers)

numbers.remove(2)
print(numbers)

del numbers[1]

print(numbers)

numbers.extend([13, 17])

print(numbers)

numbers.clear()
print(numbers)

# iterating an array
numbers = [2, 3, 5, 7, 11, 13, 17]
for i in numbers:
    print(i)

# iterating over an array with index
for i in range(0, len(numbers)):
    print(i)
