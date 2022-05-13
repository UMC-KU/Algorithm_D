# 스택 연산에서 push, pop, size, empty, top 등을 구현하는 프로그램
import sys
from collections import deque
n = int(input())
stack = deque()
for i in range(n):
    inputs = sys.stdin.readline().split()
    if len(inputs) > 1:
        word, num = inputs
        num = int(num)
    else:
        word = inputs[0]
    
    if word == 'push':
        stack.appendleft(num)
    elif word == 'pop':
        if len(stack) > 0:
            print(stack.popleft())
        else:
            print(-1)
    elif word == 'size':
        print(len(stack))
    elif word == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif word == 'top':
        if len(stack) > 0:
            print(stack[0])
        else:
            print(-1)