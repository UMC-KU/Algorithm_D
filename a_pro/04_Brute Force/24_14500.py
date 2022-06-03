import sys

n, m = map(int, sys.stdin.readline().split())
board = []
blocks = (
    # l
    ((1, 1, 1, 1), ),   # 튜플은 원소 1개여도 , 꼭 붙여줄 것!
    ((1, ), (1, ), (1, ), (1, )),
    # ㅁ
    ((1, 1), (1, 1)),
    #ㄴ
    ((1, ), (1, ), (1, 1)),         # ㄴ
    ((0, 1), (0, 1), (1, 1)),   # ㄴ반대
    ((0, 0, 1), (1, 1, 1)),     # ㄴ2반대
    ((1, 0, 0), (1, 1, 1)),     # ㄴ2
    ((1, 1), (1, 0), (1, 0)),   # ㄱ반대
    ((1, 1), (0, 1), (0, 1)),   # ㄱ
    ((1, 0), (1, 0), (1, 1)),   # L
    ((0, 1), (0, 1), (1, 1)),   # L 반대
    # ㄹ
    ((1, 0), (1, 1), (0, 1)),
    ((0, 1), (1, 1), (1, 0)),
    ((0, 1, 1), (1, 1, 0)),
    ((1, 1, 0), (0, 1, 1)),
    # ㅗ
    ((1, 1, 1), (0, 1, 0)),
    ((0, 1, 0), (1, 1, 1)),
)
board_empty = [[0 for j in range(m)] for i in range(n)]
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

def solution(board_empty, point):
    global board, max_point, n, m, blocks
    for i in range(n):
        for j in range(m):
            for block in blocks:
                # over board
                if i + len(block) >= n or j + len(block[0]) >= m:
                    continue
                # board overlap
                succeed = 1
                for index_y, y in enumerate(block):
                    if not succeed:
                        break
                    for index_x, x in enumerate(y):
                        # board overlap
                        if board_empty[i+index_y][j+index_x] and x:
                            succeed = 0
                            break
                        # normal
                        if x:
                            board_empty[i+index_y][j+index_x] = 1
                            point += board[i+index_y][j+index_x]
                if succeed:
                    solution(board_empty, point)
    if point > max_point:
        max_point = point
    return
max_point = 0
res = solution(board_empty, 0)
print(max_point)