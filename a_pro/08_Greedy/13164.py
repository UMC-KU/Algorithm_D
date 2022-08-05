# 13164 : n명의 원생들을 k개의 그룹으로 쪼갤 때,
# 각 그룹에서 가장 키가 큰 원생과 작은 원생의 키차이의 합이 최소일때의 합을 출력하는 것.
# 알고리즘 - 각 아이들의 키차이를 구한뒤, 가장 차이가 큰 k-1곳을 끊어 k개의 그룹으로 만드는 것.
# 차이가 1 2 2 1 4 처럼 같은 차이가 2개 이상 연속된 경우, 어느 곳을 끊든지 간에 비용은 같음.
# 220723 solved
import sys, heapq
n, k = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
# 최소힙 조심
diff = []   # diff 길이 : k-1
point = []  # point 길이 : k-1, 들어갈 수 있는 값 : 0~ n-2
res = 0

if 1 < k < n:   # k == n이면 비용이 들지 않음.
    for i in range(n-1):
        heapq.heappush(diff, (lst[i] - lst[i+1], i))
    # 단절점 - point[x] = l, point[x+1] = m일때 비용 = lst[m] - lst[l+1]

    for i in range(k-1):
        point.append(heapq.heappop(diff)[1])

    point.sort()
    res += lst[point[0]] - lst[0]
    for i in range(1, k-1):
        res += lst[point[i]] - lst[point[i-1]+1]
    if n > 1:
        res += lst[n-1] - lst[point[k-2]+1]    # point[k-2] == n-2어도 0으로 처리됨.
elif k == 1:
    res = max(lst) - min(lst)
print(res)