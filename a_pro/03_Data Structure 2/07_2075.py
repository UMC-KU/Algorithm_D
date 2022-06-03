# n*n 테이블에서 n번째로 큰 수를 찾는 프로그램
# 최대힙 사용해 풀어도 안됨... -> 메모리초과.
# SOL : 가장 큰 수 -> 맨 밑 줄에 존재하는 점 이용
# -> 맨 밑줄에 존재하는 수들 max heap에 집어넣고, 
# pop n-1번 하면서 pop된 세로줄 맨 밑 수 추가하면 됨.
import sys, heapq
n = int(sys.stdin.readline())
table = []
for _ in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))

# max_heap 만들어서 가장 큰 수들만 n-1번 뺌.
cnt = 0
row_count = [n-2] * n
max_heap = [(-table[n-1][i], i) for i in range(n)]
#for i in [(-table[n-1][i], i) for i in range(n)]:
#    heapq.heappush(max_heap, i)
heapq.heapify(max_heap) # 각 정보마다 heappush해줘도 되지만, 리스트를 minheap으로 만들어주는 heapify함수가 있었음.

# 가장 큰 수를 하나 pop하고, 그 수가 있었던 열에서 빠진 수의 다음 수를 추가함.
while cnt < n - 1:
    j = heapq.heappop(max_heap)[1]
    heapq.heappush(max_heap, (-table[row_count[j]][j], j))
    row_count[j] -= 1
    cnt += 1
print(-max_heap[0][0])