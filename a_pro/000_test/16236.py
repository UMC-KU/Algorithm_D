# 아기 상어 문제
# 각 먹이까지의 거리를 구하고, 거리가 가까운 순으로 먹으면서 얼마나 먹을 수 있는지를 구하는 프로그램
# dfs방식 사용, 너무 시간 많이 걸림..
from sys import stdin
def search():
    global sea, n, size, bait, location
    bait[:] = []
    for i in range(n):
        for j in range(n):
            if 0 < sea[i][j] < size:    # 0도 처리해줘야함
                if size < 6:
                    temp = distance(i, j, 0, location[0], location[1])
                else:
                    temp = abs(i - location[0]) + abs(j - location[1])
                if temp > 0:
                    bait.append([temp, sea[i][j], [i, j]])
    return
# i, j 는 목표 위치, x, y는 현재 위치
def distance(i, j, cost, y, x):
    global location, size, visited
    res = -1
    visited[y][x] = 1
    temp = 0
    # 목적지 도달한 경우
    if i == y and j == x:
        visited[y][x] = 0
        #print('end', y, x)
        return cost

    if y > 0 and sea[y-1][x] <= size and not visited[y-1][x]:
        #print('->', y-1, x, end = ' ')
        temp = distance(i, j, cost+1, y-1, x)
    if temp > 0 and (res < 0 or temp < res):
        res = temp

    if x > 0 and sea[y][x-1] <= size and not visited[y][x-1]:
        #print('->', y, x-1, end = ' ')
        temp = distance(i, j, cost+1, y, x-1)
    if temp > 0 and (res < 0 or temp < res):
        res = temp

    if x < n-1 and sea[y][x+1] <= size and not visited[y][x+1]:
        #print('->', y, x+1, end = ' ')
        temp = distance(i, j, cost+1, y, x+1)
    if temp > 0 and (res < 0 or temp < res):
        res = temp
    
    if y < n-1 and sea[y+1][x] <= size and not visited[y+1][x]:
        #print('->', y+1, x, end = ' ')
        temp = distance(i, j, cost+1, y+1, x)
    if temp > 0 and (res < 0 or temp < res):
        res = temp
    
    visited[y][x] = 0
    # print('res return', res, y, x)
    return res

# 입력
n = int(stdin.readline())
sea = []
size = 2
exp = 0
time = 0
bait = []   # 먹이의 거리, 크기, 위치 정보를 담는 배열
location = []
visited = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    sea.append(list(map(int, stdin.readline().split())))
# 아기상어 처음 위치 설정
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            location = [i, j]
            break

while True:
    search()
    # 우선순위대로 정렬
    bait.sort(key=lambda bait: bait[2][1])  # [[1, 2, 3], ...]
    bait.sort(key=lambda bait: bait[2][0])
    bait.sort()
    
    
    if len(bait) < 1:
        break
    else:   # 먹기
        exp += 1
        time += bait[0][1]
        sea[location[0]][location[1]] = 0
        location[0] = bait[0][2][0] # 이동
        location[1] = bait[0][2][1]
        sea[location[0]][location[1]] = 9
        print('loc:', location, 'bait', bait)
        for i in range(n):
            print(sea[i])
        print('time', time)
    # 레벨업
    if exp == size and size < 7:    # 자기 자신 먹는경우 방지
        size += 1
        exp = 0
        print('level up', size)

print(time)