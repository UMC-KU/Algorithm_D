# 덱을 구현하는 문제
# 덱 : double ended queue, 두 곳에서 입출력이 일어날 수 있다.
from collections import deque
import sys

n = int(input())
deque_ = deque()
for _ in range(n):
    word = sys.stdin.readline().split()
    if len(word) == 1:
        word = word[0]
    else:
        num = word[1]
        word = word[0]
    if word == 'push_front':
        deque_.appendleft(num)
    elif word == 'push_back':
        deque_.append(num)
    elif word == 'size':
        print(len(deque_))
    elif word == 'empty':
            if len(deque_):
                print(0)
            else:
                print(1)
    elif len(deque_):
        if word == 'pop_front':
            print(deque_.popleft())
        elif word == 'pop_back':
            print(deque_.pop())
        elif word == 'front':
            print(deque_[0])
        elif word == 'back':
            print(deque_[-1])
    else:
        print(-1)