# 최대 힙 문제 -> 자연수 들어오면 heappush, 0이면 heappop하는 문제.
# 최대 힙 정렬하는 시간복잡도는 O(logN), 리스트는 따라올 수 없음.
import heapq, sys

heap = []
n = int(input())
for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp:
        heapq.heappush(heap, (-tmp, tmp))           # 최대힙 쓰는 요령, 음수 튜플로 집어넣고 pop값에 1번인덱스값을 쓴다.
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)