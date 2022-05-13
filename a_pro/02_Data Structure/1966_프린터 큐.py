# 굉장히 naive한 알고리즘
# 그냥 원래 리스트인 importance를 돌리면서 자기 차례가 오면(turn[index_t]와 같아지면) turn의 다음 요소로 바꿔줌.
# 그러다 d와 index_i값이 같아지는 때가 오면 내가 원하는 값이 출력된다는 뜻이므로
# 그때의 index_t값을 출력함(1 더하는게 맞음)
# index_t에는 현재 출력한 값이 몇 번째인지를(중요도 순이므로 같은 의미)
# index_i에는 현재 보고 있는 중요도 값의 인덱스가 저장됨.
# n <= 100이라 O(n^2)이지만 맞았습니다가 뜸.
# 220416 solved.
import sys
from collections import deque
t = int(input())
for _ in range(t):
    queue = deque()
    n, d = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))   # 중요도를 담고 있는 리스트
    # 정렬된 리스트를 하나 만들고, 그 리스트 각각에 있는 수를 찾을 때 까지 계속 원래 리스트를 돌리는 알고리즘.
    turn = sorted(importance, reverse=True) # 중요도를 내림차순으로 정렬한 리스트
    index_t = 0
    index_i = 0
    while 1:
        if turn[index_t] == importance[index_i]:
            index_t += 1
            if d == index_i:
                break
        index_i += 1
        index_i %= len(importance)
        index_t %= len(turn)
    print(index_t)