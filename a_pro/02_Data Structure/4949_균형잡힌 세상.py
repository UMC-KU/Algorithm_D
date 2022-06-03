# 입력받은 문자열들을 잘 처리해서 . 단위로 끊어읽고, '균형잡혔는지' 판단하는 프로그램
# 괄호 짝이 맞지 않으면 '균형잡힌' 게 아님.
import sys
from collections import deque
line = ''
stack = deque()
shape = {
    ')':'(',
    ']':'['
}

while True:
    temp = sys.stdin.readline().rstrip()
    if temp:        # EOF -> 입력 없으면 break해줌. -> 맨 마지막에 .한개 들어오는 줄 모르고 계속 처리 안해줬었음...
        line += temp    # 일단 마지막까지 계속 읽어서 계속 문자열을 합침 
    else:
        break

line = line.split('.')[:-2] # 다 받은 문자열에서 .단위로 끊고, 마지막 2개는 없앰, 1개는 점개수 +1이어서, 1개는 마지막 .때문에.
# print('line :', line)

for i in line:
    succeed = 1
    stack = deque()
    # 괄호 하나도 없으면 성공
    if i.count('(') + i.count(')') + i.count('[') + i.count(']') == 0:
        print('yes')
        continue

    for elmt in i:
        if elmt in '([':
            stack.appendleft(elmt)
        elif elmt in ')]':
            if not stack or stack.popleft() != shape[elmt]: # 스택에 값이 없어도 틀린 것.
                succeed = 0
                break
    if stack:           # 끝났을 때 스택에 남아있는게 있으면 틀린 것.
        succeed = 0
    if succeed:
        print('yes')
    else:
        print('no')