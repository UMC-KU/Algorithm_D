# 2212 : 센서
# 아까 13164와 동일한 알고리즘 적용 가능...
# 220729 solved
import sys, heapq
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()  # 센서들 좌표, 순서대로 주어지지는 않음.
diff = []

for i in range(n-1):
    heapq.heappush(diff, (lst[i]-lst[i+1], i))

length = max(lst) - min(lst)
if n <= k:  # 이부분이 point!
    length = 0
else:
    for i in range(k-1):
        tmp = -heapq.heappop(diff)[0]
        length -= tmp

print(length)