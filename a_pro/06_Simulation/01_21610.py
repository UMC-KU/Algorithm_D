import sys, copy
# 구름 영역 기본 구름 생성하는 함수, 초기화 x
def create_cloud():
    global sky, n
    if [n-2, 0] not in sky:
        sky.append([n-2, 0])
    if [n-2, 1] not in sky:
        sky.append([n-2, 1])
    if [n-1, 0] not in sky:
        sky.append([n-1, 0])
    if [n-1, 1] not in sky:
        sky.append([n-1, 1])
    return

# 구름 하나 위치 받아서 이동시키는 함수
def move(d, s):
    global sky, n
    if d == 1:
        x_move, y_move = -1, 0
    elif d == 2:
        x_move, y_move = -1, -1
    elif d == 3:
        x_move, y_move = 0, -1
    elif d == 4:
        x_move, y_move = 1, -1
    elif d == 5:
        x_move, y_move = 1, 0
    elif d == 6:
        x_move, y_move = 1, 1
    elif d == 7:
        x_move, y_move = 0, 1
    elif d == 8:
        x_move, y_move = -1, 1
    
    x_move *= s
    y_move *= s
    
    for i in range(len(sky)):
        sky[i][0] += y_move
        sky[i][1] += x_move
        sky[i][0] %= n
        sky[i][1] %= n
    return
    
def copy_water(i, j):
    global ground, rain, n
    cnt = 0
    # 대각선 방향에 물이 있을 경우, 물이 있는 바구니의 수만큼 물의 양 증가.
    if i > 0 and j > 0 and ground[i-1][j-1]:
        cnt += 1
    if i < n-1 and j > 0 and ground[i+1][j-1]:
        cnt += 1
    if i > 0 and j < n-1 and ground[i-1][j+1]:
        cnt += 1
    if i < n-1 and j < n-1 and ground[i+1][j+1]:
        cnt += 1
    rain[i][j] = cnt
    return

def print_ground():
    global ground, n
    for i in range(n):
        print(ground[i])
    return
# 입력부
n, m = map(int, sys.stdin.readline().split())
ground = []
rain = [[0 for i in range(n)] for j in range(n)]    # 물복사버그 일으킬때 저장하는 배열
orders = []
sky = []        # 구름 좌표만, [i, j] 형식으로 저장
new_sky = []
for i in range(n):
    ground.append(list(map(int, sys.stdin.readline().split())))

for i in range(m):
    orders.append(list(map(int, sys.stdin.readline().split())))

# 비바라기 실행
cloud_existed = []
for order in orders:
    rain[:] = [[0 for i in range(n)] for j in range(n)]
    create_cloud()
    move(order[0], order[1])
    # 비바라기 -> 그름이 있는 칸에 물의 양 1 증가
    for cloud in sky:
        x, y = cloud[1], cloud[0]
        ground[y][x] += 1
    # for cloud in new_sky:
    #     x, y = cloud[1], cloud[0]
    #     ground[y][x] += 1
    
    print('before')
    print_ground()
    # 원래 여기서 구름 삭제
    cloud_existed = copy.deepcopy(sky)
    sky.clear()
    new_sky.clear()
    # 물복사버그 사용
    for cloud in cloud_existed:
        x, y = cloud[1], cloud[0]
        copy_water(y, x)
    for cloud in cloud_existed:
        x, y = cloud[1], cloud[0]
        ground[y][x] += rain[y][x]
    
    print('ground: ')
    print_ground()
    
    # 물의 양이 2 이상인 칸에 구름이 생기고, 양이 2 줄어듦.
    for i in range(n):
        for j in range(n):
            if ground[i][j] >= 2 and [i, j] not in cloud_existed:
                ground[i][j] -= 2
                new_sky.append([i, j])
    print('sky :')
    print(sky)
# 합계 출력
res = 0
for i in range(n):
    for j in range(n):
        if ground[i][j]:
            res += ground[i][j]
print(res)
