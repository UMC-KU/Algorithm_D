from collections import deque
words = input()
stack = deque()
for i in words:
    if ord('A') > ord(i) or ord(i) > ord('Z'):
        if i == '(':
            
        stack.appendleft(i)
print(stack