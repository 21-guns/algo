from collections import deque

instack = deque()
instack.append(1)
instack.append(3)
instack.append(5)

first = instack.pop()
second = instack.pop()
third = instack.pop()

print(first, second, third)