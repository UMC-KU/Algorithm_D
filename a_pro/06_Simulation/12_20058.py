# 220629 - BOJ 20058 마법사 상어와 파이어스톰
# dfs, 배열 회전 사용.
import sys, copy
# 얼음의 크기를 구하는 알고리즘
def dfs(i, j, cnt):
    global grid, visited, size
    # 이번이 첫 방문한 노드일때
    # 첫 방문 노드가 비어 있을 가능성도 생각해야함.
    if cnt == 0:
        visited[i][j] = 1
        cnt += 1
    # 범위 validation 그냥 try except로 해줄 수도 있음!
    # 최댓값만 return해주려면 cnt에 더해 주는 것이 아니라 그대로 값을 입력해줘야함.
    # 어차피 나오는 값은 현재 값보다 크거나 같음.
    if i > 0 and grid[i-1][j] and not visited[i-1][j]:
        visited[i-1][j] = 1
        cnt = dfs(i-1, j, cnt+1)
    if j > 0 and grid[i][j-1] and not visited[i][j-1]:
        visited[i][j-1] = 1
        cnt = dfs(i, j-1, cnt+1)
    if i < size-1 and grid[i+1][j] and not visited[i+1][j]:
        visited[i+1][j] = 1
        cnt = dfs(i+1, j, cnt+1)
    if j < size-1 and grid[i][j+1] and not visited[i][j+1]:
        visited[i][j+1] = 1
        cnt = dfs(i, j+1, cnt+1)
    return cnt

# 배열 회전시키는 함수, 
# q는 파이어스톰 단계별 Li
# grid는 기존의 얼음 정보 저장하는 배열
# t_grid에 복사한 이후, 다시 grid에 넣어서 저장.

# 최소단위 (한변의길이 = 2**(q+1)인 정사각형)를 2**(n-q-1)번 반복하면 전체 모양이 됨.
# 최소단위 안에서는 2**q인 회전 영역만 2번 회전시켜주면 됨.
def rotate(q):
    global grid, size, n
    steps = 2**(n-q)    # 한 변에 존재하는 회색 부분의 개수
    t_grid = [[0 for i in range(size)]for j in range(size)]
    # 최소 단위 반복
    for ki in range(0, 2**n, 2**(q+1)):
        for kj in range(0, 2**n, 2**(q+1)):
            # 최소 단위 내에서 2**q인 정사각형 2번 반복
            sti = 0
            stj = 0
            # q == n이면 리스트 범위를 넘어가버림
            # 그렇다고 2**n보다 작을때로 하면 너무 커져버림. 
            # 2**q보다는 작거나 같아야함.
            while sti <= 2**q and sti < 2**n:
                # 한 변의 크기가 2**l인 정사각형 회전
                for i in range(2**q):
                    for j in range(2**q):
                        t_grid[ki+sti+j][kj+stj+2**q-1-i] = grid[ki+sti+i][kj+stj+j]
                sti += 2**q
                stj += 2**q
    # 나머지 부분은 그대로 복사
    for ki in range(0, 2**n, 2**(q+1)):
        for kj in range(0, 2**n, 2**(q+1)):
            if q < n:
                for sti, stj in zip([2**q, 0], [0, 2**q]):
                    for i in range(2**q):
                        for j in range(2**q):
                            t_grid[ki+sti+i][kj+stj+j] = grid[ki+sti+i][kj+stj+j]
    grid = copy.deepcopy(t_grid)
    return

# 주변 얼음이 존재하는 칸수 세주는 함수, i, j는 기준 칸 좌표
def cnt_ice(i, j):
    global size
    cnt = 0
    if i > 0 and grid[i-1][j]:
        cnt += 1
    if j > 0 and grid[i][j-1]:
        cnt += 1
    if i < size - 1 and grid[i+1][j]:
        cnt += 1
    if j < size - 1 and grid[i][j+1]:
        cnt += 1
    return cnt
    
# visited 초기화해주는 함수
def init_visited():
    global visited, size
    for i in range(size):
        for j in range(size):
            visited[i][j] = 0
    return

# 입력부
n, q = map(int, sys.stdin.readline().split())
grid = []
step = []
size = 2**n
visited = [[0 for i in range(size)] for j in range(size)]
# grid 입력
for i in range(size):
    grid.append(list(map(int, sys.stdin.readline().split())))
# 마지막줄 Li 입력
step = list(map(int, sys.stdin.readline().split()))

# process per steps
for q in step:
    rotate(q)
    print()
    melt = []
    for i in range(size):
        for j in range(size):
            if cnt_ice(i, j) < 3 and grid[i][j] > 0:
                melt.append([i, j])  
    # 바로바로 녹이지 말고, 한 번 지울 대상을 정한 후 녹일 것.
    # 중간에 녹이다가 새로 녹일 대상이 생길 수 있음.
    for coord in melt:
        grid[coord[0]][coord[1]] -= 1

res = 0
max_ice_size = 0
for i in range(size):
    for j in range(size):
        # 첫 방문 노드가 비어 있을 가능성도 생각해야함.
        if grid[i][j]:
            # 최대 얼음 크기 구함
            init_visited()
            temp = dfs(i, j, 0)
            if max_ice_size < temp:
                max_ice_size = temp
            # 남아있는 총 얼음 합 구함    
            res += grid[i][j]
# output
for i in range(2**n):
    print(grid[i])
print(res)
print(max_ice_size)