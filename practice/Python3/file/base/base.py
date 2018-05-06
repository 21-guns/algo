import os
import os.path
import shutil
import time

# check if the file exists
file_name = "file.txt"
exists = os.path.exists(file_name)
print(exists)
if not exists:
    with open(file_name, 'w') as f:
        pass

# copy a directory

src = os.path.join(os.getcwd(), "data")
dst = os.path.join(os.getcwd(), "data_copy")

try:
    shutil.copytree(src, dst)
# create a directory
except FileNotFoundError as no_file_error:
    os.makedirs(src, exist_ok=True)
except Exception as e:
    print("Error happened " + e.__str__())

# create a directory
test_directory = dst
if not os.path.exists(os.path.join(os.getcwd(), test_directory)):
    os.makedirs(test_directory, exist_ok=True)

# delete a directory
try:
    # base delete
    os.rmdir(test_directory)
    # delete data
    shutil.rmtree(test_directory)
except Exception as e:
    print("Error happened " + e.__str__())

# copy a file

src = os.path.join(os.getcwd(), file_name)
dst = os.path.join(os.getcwd(), "file_copy.txt")

try:
    # data copy
    shutil.copy(src, dst)
    # copy with metadata and permissions
    shutil.copy(src, dst)
except Exception as e:
    print("Error happened " + e.__str__())

# delete file
try:
    os.remove(dst)
except Exception as e:
    print("Error happened " + e.__str__())

# move file
try:
    shutil.move(file_name, "file_move.txt")
    shutil.move("file_move.txt", file_name)
except Exception as e:
    print("Error happened " + e.__str__())

# get working directory

path = os.getcwd()
print(path)
# or
path = os.path.dirname(os.path.realpath(__file__))
print(path)

# get file properties

# file size
file_size = os.path.getsize(file_name)
# file modification date
date_modified = time.ctime(os.path.getmtime(file_name))
# file size
creation_date = time.ctime(os.path.getctime(file_name))
# is readable file
is_readable = os.access(file_name, os.R_OK)
# is writeable file
is_writeable = os.access(file_name, os.W_OK)
# file name and extension
name_only, extension = os.path.splitext(os.path.basename(file_name))
# file path
file_path = os.path.dirname(file_name)

print(file_size)
print(date_modified)
print(creation_date)
print(is_readable)
print(is_writeable)
print(name_only, extension)
print(file_path)

# list files in a directory
file_dir = os.getcwd()
files = [f for f in os.listdir(file_dir)]
print(files)
