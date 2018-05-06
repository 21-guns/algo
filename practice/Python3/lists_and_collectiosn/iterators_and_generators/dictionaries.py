# elements count
import operator

dic = {
    1: "A",
    3: "C",
    2: "B"
}

print(len(dic))
print(dic.__len__())

# get value by key
print(dic.get(1))
print(dic[1])

# sort dic
sorted_dic = sorted(dic.items(), key=operator.itemgetter(0))
print(dict(sorted_dic))
sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))

# dictionaries initialization
print(dict(sorted_dic))

# get dic keys
print(dic.keys())
# get dic value
print(dic.values())

# checking of presence of a key
print(1 in dic)
print(10 in dic)

# adding and removing of elements
del dic[2]
print(dic)
dic.clear()
print(dic)

# iterating over a dictionary
for key, value in dic.items():
    print(key, value)




