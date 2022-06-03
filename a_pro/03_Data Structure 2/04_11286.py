# 절댓값 힙
# 최소 힙처럼 구현하지만 사실 절댓값이 가장 작은 값을 출력, 
# 절댓값이 같은 값이 여러개면 가장 작은 수 출력.
# 그냥 최소힙과는 차이가 있음. 
# 최대힙 구현 방식과 비슷하게 구현.

import heapq, sys
n = int(input())
heap = []
for _ in range(n):
    temp = int(sys.stdin.readline().split()[0])
    if temp:    # temp != 0일때 -> push
        heapq.heappush(heap, (abs(temp), temp))
    else:
        if heap:
            heap_tmp = []   # 임시로 heap에서 빼온 값을 저장하는 리스트
            heap_tmp.append(heapq.heappop(heap))
            # 힙에서 pop된 것과 첫 번째 수(절댓값)가 같은 것이 있으면 다 pop함
            while heap and heap[0][0] == heap_tmp[0][0]:
                heap_tmp.append(heapq.heappop(heap))
            # pop된것들을 모아 놓은 리스트에서 두 번째 인덱스의 값이 최소인 것을 구하고 그 인덱스를 저장함
            min = heap_tmp[0][0]
            minIndex = 0
            for index, element in enumerate(heap_tmp):
                if element[1] < min:
                    min = element[1]
                    minIndex = index
            print(min)
            # 다시 넣어줌
            del heap_tmp[minIndex]
            for i in heap_tmp:
                heapq.heappush(heap, i)
        else:
            print(0)

# 절댓값 힙, 음수 힙으로 구현. 절댓값 힙은 최대 힙처럼 사용해서 해보기.