# 소마 코테에서 본 문제
# 단지 개수만 같아야 하는 게 아니라, 괄호 안에 감싸져 있어야 함.
# 그래서 )(같은 케이스를 방지하기 위해 cnt값을 증감시키며 판단함.
import sys
t = int(input())
for i in range(t):
    word = input()
    cnt = 0
    for j in word:
        if j == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0: # 이미 안됨.
            break
    if cnt == 0:
        print('YES')
    else:
        print('NO')