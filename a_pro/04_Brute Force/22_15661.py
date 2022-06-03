# 링크와 스타트 -> 38%
import sys
from itertools import combinations
from itertools import product
# 팀과 표를 입력받아서 그 능력치를 반환하는 함수
def team_str(lst, s):
    res = 0
    for i in combinations(lst, 2):
        y = i[0]
        x = i[1]
        res += s[y][x]    # 순서상관 없는경우므로 두개 더해줌.
        res += s[x][y]
    return res

n = int(sys.stdin.readline())
s = []
for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))

min_res = 100
case = list(product(*((1, 0) for _ in range(n))))
# 어차피 스타트, 링크팀으로 나눠지므로 절반의 경우만 시도해주면 됨.
for i in case[:len(case)]:
    start = []
    link = []
    for index, j in enumerate(i):
        if j:
            start.append(index)
        else:
            link.append(index)
    res_start = team_str(start, s)
    res_link = team_str(link, s)
    if (start and link) and min_res > abs(res_start - res_link):
        min_res = abs(res_start - res_link)
print(min_res)