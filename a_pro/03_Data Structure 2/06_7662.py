# 이중 우선순위 큐 만드는 프로그램
# 이진탐색 사용 -> insert 때문에 실패
# 이중 우선순위 큐
import sys, heapq

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    min_heap = []
    max_heap = []
    exist = [False] * 1000001   # i번째 입력을 받았을 때, 해당 입력이 heap에 있는지를 체크해주는 리스트
    k = int(sys.stdin.readline().rstrip())
    for i in range(k):
        ch, n = sys.stdin.readline().split()
        n = int(n)
        if ch == 'I':
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
            exist[i] = True
        else:
            if n > 0:
                while min_heap and not exist[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                # 만약 if문을 먼저 만나면 heap에서 빼는 수가 없는 수인지 모름. 그래서 먼저 정리해주고 빼줘야함.
                if max_heap:
                    exist[heapq.heappop(max_heap)[1]] = False
            else:
                while max_heap and not exist[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if min_heap:
                    exist[heapq.heappop(min_heap)[1]] = False

    # if문이 뒤에 있으므로 마지막에 한번 정리를 해줘야 함.
    while min_heap and not exist[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not exist[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if max_heap:
        # 최대, 최솟값 출력
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')