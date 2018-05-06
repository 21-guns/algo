import pickle

# read and using buffer

file_name = "file.out"
file_name_copy = "file.copy.out"

buffer_size = 1024

with open(file_name, 'rb') as rf:
    with open(file_name_copy, 'wb') as wf:
        data = rf.read(buffer_size)
        while data:
            wf.write(data)
            data = rf.read(buffer_size)

# write array
array_file = "array.txt"
numbers = [1, 2, 3]
with open(array_file, 'wb') as wf:
    pickle.dump(numbers, wf, pickle.HIGHEST_PROTOCOL)

# read array
with open(array_file, "rb") as rf:
    numbers = list(pickle.load(rf))
    print(numbers)

# write dict
dic_file = "dict.txt"
dic = {
    "one": 1,
    "two": 2
}
with open(dic_file, 'wb') as wf:
    pickle.dump(dic, wf, pickle.HIGHEST_PROTOCOL)

# read dict
with open(dic_file, "rb") as rf:
    read_dic = dict(pickle.load(rf))
    print(read_dic)

# write binary
byte_file = "binary.txt"
byte_data = {
    "one": 1,
    "two": 2
}
with open(byte_file, 'wb') as wf:
    pickle.dump(numbers, wf, pickle.HIGHEST_PROTOCOL)

# read dict
with open(byte_file, "rb") as rf:
    data = rf.read()
    list_data = list(data)
    print(list_data)
