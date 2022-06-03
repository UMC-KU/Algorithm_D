# 0514
# IDEA : 리스트 오른쪽에서부터 스택이 비어 있다면 값을 담고,
# 스택에 값이 있다면 그 값이 현재 인덱스의 값보다 작은 값들일때 
# res리스트에 그 작은 값들의 인덱스에 접근해 현재 인덱스를 입력함.
# 
# 스택에 담겨 있는 값들은 자기보다 큰 값이 나올 때까지 기다리는 것.
# 매 요소 하나하나마다 그 요소의 왼쪽의 값들을 비교해줄 필요가 없는 것이 인상적이었음.
from collections import deque
n = int(input())
towers = list(map(int, input().split()))

stack = deque()
res = [0] * len(towers)
for i in range(len(towers)-1, -1, -1):
    while stack and towers[stack[0]] < towers[i]:
        res[stack.popleft()] = i+1
    stack.appendleft(i)

print(' '.join(map(str, res)))