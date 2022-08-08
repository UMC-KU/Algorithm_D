# 구간 합 구하기
import sys
n, m = map(int, sys.stdin.readline().split())
board = []
coordinates = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
for i in range(m):
    coordinates.append(list(map(int, sys.stdin.readline().split())))

for case_num in range(m):
    sum = 0
    for i in range(coordinates[case_num][0], coordinates[case_num][2]+1):
        for j in range(coordinates[case_num][1], coordinates[case_num][3]+1):
            sum += board[i-1][j-1]
    print(sum)