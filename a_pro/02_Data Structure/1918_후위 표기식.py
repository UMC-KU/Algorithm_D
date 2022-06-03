# 미완
from collections import deque
words = input()
ch = ('+', '-', '*', '/', '(', ')')
stack = deque() # 연산자 저장하는 스택
for i in words:
    if i in ch:
        if stack:
            if i in '*/' and stack[0] in '+-':

        else:
            stack.appendleft(i)