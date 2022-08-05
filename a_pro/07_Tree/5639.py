# 완전 이진 트리를 전휘 순회(루트-왼쪽-오른쪽)한 결과가 주어졌을 때
# 이를 후위 순회(왼쪽-오른쪽-루트)한 순서를 출력하는 프로그램
# not solved
import sys, heapq
def makeGraph(nodeIdx, nextIdx):
    global graph, frontSearch, n

    # 왼쪽노드 추가하는 경우
    if nextIdx < n and not graph[frontSearch[nodeIdx]][0] and frontSearch[nodeIdx] > frontSearch[nextIdx]:
        graph[frontSearch[nodeIdx]][0] = frontSearch[nextIdx]
        graph[frontSearch[nextIdx]][2] = frontSearch[nodeIdx]
        nextIdx = makeGraph(nextIdx, nextIdx+1)
    
    # 오른쪽노드 추가하는 경우
    if nextIdx < n and not graph[frontSearch[nodeIdx]][1]:
        checknode = frontSearch[nodeIdx]
        # 부모 노드보다 클 때 계속 타고 올라감
        while checknode != frontSearch[0] and graph[checknode][2] < frontSearch[nextIdx]:
            checknode = graph[checknode][2]
        graph[checknode][1] = frontSearch[nextIdx]
        graph[frontSearch[nextIdx]][2] = checknode
        
        return makeGraph(frontSearch.index(checknode), nextIdx+1)


    return nextIdx

# 후위 순회
def trackBackwards(node, stack):
    global graph, result


frontSearch = []
graph = dict()
stack = []
try:
    while True:
        frontSearch.append(sys.stdin.readline())
except:
    n = len(frontSearch)
    # graph 초기화
    i = 0
    while i < n-1:
        graph[frontSearch[i]] = [0, 0, 0]   # 왼쪽노드, 오른쪽노드, 부모노드. 크기순 1, 3, 4
        i += 1
    makeGraph(0, 1)
    
    result = [0 for i in range(n)]
    

