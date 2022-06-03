# 0527 SOLVED
import sys
from itertools import product

# 주어진 배열 내의 모든 신맛과 쓴맛의 조합중 가장 차이가 작은 경우의 차이를 출력하는 프로그램
n = int(sys.stdin.readline())
s = []  # 신맛 배열
b = []  # 쓴맛 배열
for _ in range(n):
    s.append(0)
    b.append(0)
    s[-1], b[-1] = map(int, sys.stdin.readline().split())
    # 이런 방식으로 한 번에 두개씩 입력

min = 1_000_000_000
# 모든 조합의 경우를 구하기 위해 중복순열 사용.
for i in product(*((1, 0) for _ in range(n))):  # * 붙여줘야 괄호 풀림.
    ssin = 1    # 신맛
    sson = 0    # 쓴맛
    cnt = 0
    for index, use in enumerate(i):
        if use:
            if not cnt:
                cnt = 1
            ssin *= s[index]
            sson += b[index]
    if cnt and abs(ssin - sson) < min:
        min = abs(ssin - sson)
print(min)