# change the case of characters
str = "Lower and upper"

print(str.lower())
print(str.upper())

# Escaping characters
str = "she said \"hello\" to me"
print(str)

# remove spaces
s = "  spaces "
print(s.strip())

# substring index

data_string = "Substring index"
index = data_string.find('string')
print(index)

# converting to a number
from locale import *

str_number = "42"
number = int(str_number)
print(number)

str_pi = "3.1415926"
float_pi_1 = float(str_pi)
float_pi_2 = atof(str_pi)
print(float_pi_1)
print(float_pi_2)

data_string = "Substring index"
print(data_string[:9])
print(data_string[:9][3:])


# replaces
data_string = "3, 2, 1, go!"
print(data_string.replace("1", "One").replace("2", "Two").replace("3", "Three"))
