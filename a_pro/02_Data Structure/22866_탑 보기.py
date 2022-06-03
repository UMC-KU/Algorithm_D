# 계속 런타임 에러났었는데, sys.stdin.readline()이랑 += list(stack) 바꿔주니까 
import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
buildings = list(map(int, sys.stdin.readline().split()))
lst = [deque() for i in range(n)]   # 이중 deque는 필요 x

stack = deque() # 건물 오름차순으로 저장하는 스택, 자기보다 작은 건물이 왔을 때는 stack의 맨 앞 값만 비교해 주면 한 쪽에서 보이는 건물들을 알 수 있다.
idx = 0
while idx < n: # 왼쪽에서 오른쪽으로, 왼쪽에 보이는 건물들 추가
    # 자기보다 작거나 같은 건물들 있으면 다 빼줌
    while stack and buildings[stack[0]] <= buildings[idx]:
        stack.popleft()
    # 스택에는 자기보다 큰 건물들만 남았으므로 lst에 추가
    if stack and buildings[stack[0]] > buildings[idx]:
        lst[idx].extend(stack)
        stack.appendleft(idx)
    elif not stack:
        stack.appendleft(idx)
    idx += 1

stack = deque()
idx = n - 1
while idx >= 0: # 오른쪽에서 왼쪽으로, 오른쪽에 보이는 건물 추가
    while stack and buildings[stack[0]] <= buildings[idx]:
        stack.popleft()
    if stack and buildings[stack[0]] > buildings[idx]:
        # 만약 stack의 맨 앞 값(idx+1번째 값)이 stack[0]보다 더 가깝다면
        if lst[idx] and stack[0] - idx < idx - lst[idx][0]:
            lst[idx].extendleft(stack)
        else:
            lst[idx].extend(stack)
        stack.appendleft(idx)
    elif not stack:
        stack.appendleft(idx)
    idx -= 1

for i in range(n):
    if lst[i]:
        print(len(lst[i]), lst[i][0] + 1)
    else:
        print(0)