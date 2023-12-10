from collections import deque

queue = deque()
queue.append(2)
queue.append(2)
queue.clear()
queue.append(3)
queue.appendleft(4)

queue.extend([2,4,4,5,5])
queue.extendleft([0,0,0])

print(queue.index(3))
print(queue.count(4))

print(queue)
