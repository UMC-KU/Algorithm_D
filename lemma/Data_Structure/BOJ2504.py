# 괄호의 값

import sys
from collections import deque

line = sys.stdin.readline().strip()

stack = []  # (), []
temp = ""  # stack에서 pop한 값

calc_stack = deque()  # 계산해야 하는 값들
calc = 0  # 계산 결과값 -> stack에 push

result = 0
result_status = True
status = False

for l in line:
    # 열린 괄호 -> push
    if l == "(" or l == "[":
        stack.append(l)

    # 닫힌 괄호 -> 해당 짝까지 pop
    elif l == ")":
        while temp != "(" and len(stack) > 0:
            temp = stack.pop()
            calc_stack.append(temp)
            if temp == "(":
                status = True

        if not status:  # 해당 짝이 없었다면 종료
            result_status = False
            break
        else:
            status = False

    elif l == "]":
        while temp != "[" and len(stack) > 0:
            temp = stack.pop()
            calc_stack.append(temp)
            if temp == "[":
                status = True

        if not status:  # 해당 짝이 없었다면 종료
            result_status = False
            break
        else:
            status = False

    # 괄호 이외의 입력 시 종료
    else:
        result_status = False
        break

    # 닫힌 괄호 -> calc_stack에 들어간 값 계산 & 결과값을 stack에 push
    if l == ")" or l == "]":
        if len(calc_stack) > 1:  # calc_stack에 값이 2개 이상 들어갔다면 (괄호가 2개 이상 들어갔다면 바로 종료!)
            temp = calc_stack.popleft()
            if temp != "(" and temp != "[":  # temp가 숫자일 경우
                calc += temp

                temp = calc_stack.popleft()
                if temp != "(" and temp != "[":  # 2번째 pop한 값도 숫자일 경우 -> 숫자끼리 전부 더하고 마지막에 곱하기
                    calc += temp

                    while len(calc_stack) > 1:
                        temp = calc_stack.popleft()
                        calc += temp

                    temp = calc_stack.popleft()  # 괄호만 남은 상황
                    if temp == "(":
                        calc *= 2
                    else:
                        calc *= 3

                else:  # 2번째 pop한 값이 괄호인 경우 -> 곱하기 (단, calc_stack에 값이 더 남아 있으면 안됨)
                    if len(calc_stack) == 0:
                        if temp == "(":
                            calc *= 2
                        else:
                            calc *= 3
                    else:
                        result_status = False
                        break

            else:  # temp가 괄호일 경우 -> 짤
                result_status = False
                break

        else:
            temp = calc_stack.popleft()
            if temp == "(":
                calc += 2
            else:
                calc += 3

        stack.append(calc)
        calc = 0
        temp = ""

if not result_status:
    print(0)
elif "(" in stack or "[" in stack:
    print(0)
else:
    for s in stack:
        result += s
    print(result)
