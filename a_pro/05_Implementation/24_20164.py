# 세자리 이상의 수일때, 두 자리 수일때, 한 자리 수일때
# 각각의 단계에서 규칙에 따라 나온 수들의 각 자리의 홀수의 개수가
# 최대일 경우랑 최소일 경우의 결과를 출력하는 프로그램
# 
# 세자리 이상 - 적당한 두 군데를 골라 수를 자르고, 잘린 수들을 서로 더한다.
# 두자리 - 각 자리 수를 더해 반환
# 한자리 - 프로그램 종료.
from itertools import combinations
n = int(input())
max_result = 0
min_result = -1 # 최소 
# 두 자리를 처리하는 함수
def tenth(num):
    res = num // 10 + num % 10
    return res
# 세 자리 이상일때의 수를 처리하는 함수
def hundredth(num, c1, c2):
    return int(str(num)[:c1]) + int(str(num)[c1:c2]) + int(str(num)[c2:])

# max는 홀수의 개수 넘겨주는 매개변수. 처음에는 최대 개수만 구하는줄 알았음.
def find_odd(num, max):
    global max_result
    global min_result
    temp = 0
    # 처음 한 번만 숫자를 연산하기 전에 홀수 개수를 세주면 됨.
    # 오히려 연산후 또 세주면 중복.
    for i in str(num):
        if int(i) % 2 == 1:
            max += 1
    if len(str(num)) > 2:
        for i in combinations(range(1, len(str(num))), 2):
            temp = hundredth(num, i[0], i[1])
            find_odd(temp, max)
    elif len(str(num)) == 2:
        temp = tenth(num)
        find_odd(temp, max)
    else:
        if max > max_result:
            max_result = max
        if min_result > max or min_result < 0:
            min_result = max
    return

# max, min result는 전역변수.
find_odd(n, 0)
print(min_result, max_result)