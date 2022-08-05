<<<<<<< HEAD
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
=======
from collections import deque
words = input()
stack = deque()
for i in words:
    if ord('A') > ord(i) or ord(i) > ord('Z'):
        if i == '(':
            
        stack.appendleft(i)
print(stack
>>>>>>> ff6ca0fca920a09cc250233198693a126e6da881
