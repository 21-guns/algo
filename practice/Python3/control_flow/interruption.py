# break
i = 7
f7 = 1

while True:
    f7 *= i
    i -= 1
    if i == 1:
        break

# continue
for i in range(10):
    continue
    print(i)

# for else
for i in range(10):
    continue
    print(i)
else:
    print("End")