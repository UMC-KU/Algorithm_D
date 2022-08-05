import sys
def dfs(graph, v):
    

n, m, v = map(int, sys.stdin.readline().split())
graph = [[0 for i in range(n)] for j in range(n)]
visited = [[0 for i in range(n)] for j in range(n)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1


