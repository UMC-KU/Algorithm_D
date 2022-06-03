import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, d = map(int, sys.stdin.readline().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    # 각도에 따라 돌아가도록, 음수면 360 더해서 돌아가도록 설정.
    d %= 360
    rotate = d // 45
    for go in range(rotate):
        temp = [arr[0+i][0+i] for i in range(n-1//2)]
        for i in range((n-1)//2):
            # 각 대각선 하나하나 설정
            arr[0+i][0+i] = arr[(n-1)//2][0+i]
            arr[(n-1)//2][0+i] = arr[n-1-i][0+i]
            arr[n-1-i][0+i] = arr[n-1-i][(n-1)//2]
            arr[n-1-i][(n-1)//2] = arr[n-1-i][n-1-i]
            arr[n-1-i][n-1-i] = arr[(n-1)//2][n-1-i]
            arr[(n-1)//2][n-1-i] = arr[i][n-1-i]
            arr[i][n-1-i] = arr[i][(n-1)//2]
            arr[i][(n-1)//2] = temp[i]
    # 출력
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = ' ')
        print()