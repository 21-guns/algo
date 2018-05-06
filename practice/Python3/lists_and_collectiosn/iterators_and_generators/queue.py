from collections import deque

ini_queue = deque()
ini_queue.append(1)
ini_queue.append(3)
ini_queue.append(5)

print(ini_queue.popleft())
print(ini_queue.popleft())
print(ini_queue.popleft())