from enum import Enum

# conversion from a string
class Season(Enum):
    Summer, Fall, Winter, Spring = range(4)


str_value = "Summer"
summer = None

for item in list(Season):
    if item.name == str_value:
        summer = item
        break


print(summer)
print(summer.name)
print(summer.value)

# conversion to a string
winter = Season.Winter
str_value = str(winter)
print(str_value)
str_name = winter.name
print(str_name)

# get the list of values
print(list(Season))

print(Season(2))