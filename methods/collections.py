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

# ===============================================

from collections import ChainMap
""" 
    In contrast, writes, updates, and deletions only operate on the first
     mapping.
"""

c1 = {
    'amir': 12,
    'ali': 13,
    'ahmad': 14,
    'alice': 15
}

c2 = {
    'reza': 20,
    'ramin': 21
}

c3 = {'hossein': 22}


print(ChainMap(c1, c2, c3))