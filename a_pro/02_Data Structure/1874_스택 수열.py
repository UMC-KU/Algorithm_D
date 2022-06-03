# 주어진 수열을 1~n 까지 순서대로 있는 수열을 stack을 이용하여 만들 수 있는지를 구하는 프로그램
# 중간에 구하려는 수열의 수보다 stack에 있는 값이 커버리면 실패.
# stack에는 숫자를 순서대로 넣으므로 stack의 값이 더 커버리면 방법이 없음.
# 계속 넣다~뺐다 하는 식으로 해야함. 
import sys
from collections import deque
n = int(input())
lst = []
log = ['+']
stack = deque([1])
success = 1

for _ in range(n):
    lst.append(int(sys.stdin.readline().strip('\n')))

index = 0
i = 2
while index < n:
    if len(stack) == 0 or stack[0] < lst[index]:
        stack.appendleft(i) # push
        log.append('+')
        i += 1
    elif stack[0] == lst[index]:
        stack.popleft()
        log.append('-')     # pop
        index += 1
    elif stack[0] > lst[index]:
        success = 0
        break
if success:
    for i in log:
        print(i)
else:
    print('NO')