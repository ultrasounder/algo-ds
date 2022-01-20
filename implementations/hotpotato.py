from collections import deque

def hot_potato(names, name):
    queue = deque()

    for name in names:
        queue.appendleft(queue.name)
    while len(queue) > 1:
        for _ in range(num):
            queue.appendleft(queue.pop())
            
        queue.pop()
    return queue.pop()

print(hot_potato(('Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'), 9))

            