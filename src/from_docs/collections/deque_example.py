from collections import deque

# Its advantage is that it's faster than regular list
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
print(queue)
queue.remove(2)
print(queue)
queue.pop()
print(queue)
queue.popleft()
print(queue)
