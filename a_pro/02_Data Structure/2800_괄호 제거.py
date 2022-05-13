from itertools import product
from collections import deque
line = list(input())
queue = deque()
res = []

# 괄호 쌍 위치 queue에 넣어줌
index = 0
while index < len(line):
    if line[index] == '(':
        level = 0
        tmp = index + 1
        while tmp < len(line) and level >= 0:
            if line[tmp] == ')' and level == 0:
                queue.append((index, tmp))
                break
            elif line[tmp] =='(':
                level += 1
            elif line[tmp] == ')':
                level -= 1
            tmp += 1
    index += 1

# 케이스마다 들어가야 할 괄호만 res에 추가
level = 0
lst = [[0, 1] for _ in range(len(queue))]   # 가능한 경우의 조합을 모두 만들어줌
for i in product(*lst):
    # 마지막 모두 1인 경우 제외
    if sum(i) == len(i):
        break
    res.append([])
    
    for j in line:
        if j not in '()':
            res[-1].append(j)
        else:
            if j == '(':
                level += 1
            if i[level-1]:
                res[-1].append(j)
            if j == ')':        # 이렇게 괄호 증감식 배치 안하면 출력시 순서 뒤죽박죽됨
                level -= 1

for i in sorted(res):
    for j in i:
        print(j, end='')
    print()