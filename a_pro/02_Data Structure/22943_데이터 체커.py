# 0514
# 데이터 체커, 스택 이용.
import sys
from collections import deque
# 두 원의 관계 확인해주는 함수, 1이면 겹치고 0이면 겹치지 않는 것.
def check(x1, r1, x2, r2):
    if abs(r1 - r2) <= abs(x2 - x1) <= r1 + r2:
        return 1
    return 0

succeed = 1
n = int(sys.stdin.readline())
circle = []
for _ in range(n):
    circle.append(tuple(map(int, sys.stdin.readline().split())))

# x좌표 순으로 일단 정렬해서 x축 왼쪽부터 가면서 확인함. 
circle.sort()
temp = deque() # 스택처럼 활용
temp.append(circle[0])
i = 1
while i < len(circle):
    if not succeed:
        break
    # temp에 값이 비어 있다면 현재값을 추가한 후 다음으로 넘어감.
    if temp:
        x1, r1 = temp[0]
        x2, r2 = circle[i]
    else:
        temp.appendleft(circle[i])
        i += 1
        continue
    # 일단 겹치는지 체크
    if check(*temp[0], *circle[i]):
        succeed = 0
        break
    else:
        # 안에 있다면 
        if abs(x2 - x1) < abs(r2 - r1):
            # 나중 것이 이전 것을 포함할 경우 -> 이전 것 스택에서 지우고 다시.
            if r1 < r2:
                temp.popleft()
                continue
            # 기존 것이 다음 것을 포함할 경우 -> 하나 건너뜀.
            else:
                i += 1
        # 밖에서 독립적인 경우 -> 스택에 하나 추가하고 넘어감
        else:   
            temp.appendleft(circle[i])
        i += 1
        
if succeed:
    print('YES')
else:
    print('NO')