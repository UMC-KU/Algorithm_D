# 이중 우선순위 큐 만드는 프로그램
import sys, heapq
t = int(sys.stdin.readline().rstrip())
min_heap = []
max_heap = []
for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    for __ in range(k):                                 # 한 테스트 케이스당
        ch, n = sys.stdin.readline().split()
        n = int(n)
                                                        # insert시 -> heappush
        if ch == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, (-n, n))
        elif ch == 'D':                                 # delete시 -> min이냐 max냐
            if min_heap:
                if n > 0:
                    tmp = heapq.heappop(max_heap)       # 최댓값 삭제
                    min_heap.remove(tmp[1])             # 최소 힙에서도 삭제해줌
                else:
                    tmp = heapq.heappop(min_heap)       # 최솟값 삭제
                    max_heap.remove((-tmp, tmp))        # 최대 힙에서도 삭제
    if min_heap:                                        # 어차피 뭘 해도 둘이 개수는 같음
        print(heapq.heappop(max_heap)[1], heapq.heappop(min_heap))
    else:
        print('EMPTY')