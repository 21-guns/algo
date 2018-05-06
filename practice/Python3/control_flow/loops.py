# endless cycle
# while True:
#     pass

# do while
i = 7
f7 = 1

while True:
    f7 *= i
    i -= 1
    if i == 1:
        break

#  for in
numbers = [2, 3, 4, 11, 23, 34, 45]
sum = 0
for number in numbers:
    sum += number

print(sum)

# for in range
for i in range(11):
    print(i)

i = 5
f5 = 1
# while
while i > 1:
    f5 *= i
    i -= 1

print(f5)

