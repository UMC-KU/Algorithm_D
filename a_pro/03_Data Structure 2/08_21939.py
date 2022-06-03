# 최대힙-최소힙 동기화, 딕셔너리 이용하는 문제.
import sys, heapq
n = int(sys.stdin.readline())
max_heap_db = []
min_heap_db = []
exist = [False] * 110_000
dict_db = dict()
for _ in range(n):
    line = list(map(sys.stdin.readline().split()))
    dict_db[line[0]] = (line[1], 1)  # 번호 : (난이도, 1) 형식
    heapq.heappush(max_heap_db, (-line[1], line[0]))    # (난이도, 번호) 형식
    heapq.heappush(min_heap_db, (line[1], line[0]))

m = int(sys.stdin.readline())
for _ in range(m):
    line = sys.stdin.readline().split()
    if line[0] == 'recommend':
        x = int(line[1])
        if x > 0:   # 최댓값 출력
            print(heapq.heappush(max_heap_db))
    elif line[0] == 'add':
        p, l = map(int, (line[1], line[2]))
    else:
        p = int(line[0])
    
