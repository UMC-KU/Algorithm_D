# 큐 구현하는 문제
# push, pop, size, empty, front, back 등의 기능을 구현함.
import sys
from collections import deque
n = int(input())
queue = deque()
for _ in range(n):
    inputs = sys.stdin.readline().split()
    if len(inputs) == 1:
        word = inputs[0]
    else:
        word, num = inputs
    if word == 'push':
        queue.append(num)
    elif word == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif word == 'size':
        print(len(queue))
    elif word == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(queue) == 0:
            print(-1)
        elif word == 'front':
            print(queue[0])
        else:
            print(queue[-1])