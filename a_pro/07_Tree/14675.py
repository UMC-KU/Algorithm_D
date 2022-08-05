# 트리의 연결 정보가 주어지고, 한 점이나 연결선이 주어지면
# 그 점이나 선이 단절점이나 단절선인지 판단하는 프로그램
import sys
def is_break_point(dot):
    global node_list, n
    if len(node_list[dot]) < 2:
        return 0
    else:
        return 1

n = int(sys.stdin.readline())
# graph = [[0 for i in range(n)]for j in range(n)]
node_list = [[] for i in range(n)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    # graph[a-1][b-1] = 1
    # graph[b-1][a-1] = 1
    node_list[a-1].append(b-1)
    node_list[b-1].append(a-1)

q = int(sys.stdin.readline())
for _ in range(q):
    t, k = map(int, sys.stdin.readline().split())
    if t == 1:  # 단절점
        if(is_break_point(k-1)):
            print('yes')
        else:
            print('no')
    else:   # 단절선 -> 트리는 무조건 단절선
        print('yes')