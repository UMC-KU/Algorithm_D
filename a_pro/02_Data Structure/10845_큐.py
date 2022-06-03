import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    line = sys.stdin.readline().split()
    if len(line) > 1:
        k = line[1]
        word = line[0]
    else:
        word = line[0]
    
    if word == 'push':
        queue.append(k)
    elif word == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif word == 'size':
        print(len(queue))
    elif word == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif word == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif word == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)