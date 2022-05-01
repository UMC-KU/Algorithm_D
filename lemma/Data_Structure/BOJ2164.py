# 카드2

import sys
from collections import deque

N = int(sys.stdin.readline())
kards = deque([num for num in range(1, N + 1)])

while len(kards) != 1:
    kards.popleft()
    kards.append(kards.popleft())

print(kards[0])
