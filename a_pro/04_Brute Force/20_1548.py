import sys, heapq
from itertools import product
# 이론상 가장 작은수와 중간값은 무조건 됨. 가장 큰 수가 되냐의 문제.
def trinum(a, b, c):
    m = max(a, b, c)
    return 1 if 2 * m < a + b + c else 0
    # 파이썬 표현식 일종, c언어 ?연산자와 비슷. if/else 상태문 한 줄에 쓸 수 있음.

# 부분삼각수열 idea : 가장 작은 두 수를 구한 후 나머지 수열에서 안되는 수들을 다 거르면 됨. 
# -> 최소힙 사용해서 안되는 수 나오면 그 뒤로는 쭉 안됨.
# -> 가장 작은 두 수의 조합에서 안될 수도 있음..
# 정렬 이용하자...
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
maxlen = 0

for i in product(*((1, 0) for _ in range(n))):
    succeed= 1
    tmp_lst = []
    for index, j in enumerate(i):
        if j:
            tmp_lst.append(lst[index])
    if len(tmp_lst) < 3:
        if maxlen < len(tmp_lst):
            maxlen <= len(tmp_lst)
        continue
    heapq.heapify(tmp_lst)
    
    a = heapq.heappop(tmp_lst)
    b = heapq.heappop(tmp_lst)

    for j in tmp_lst:
        if not trinum(a, b, j):
            succeed = 0
            break
    if succeed:
        if maxlen < len(tmp_lst):
            maxlen = len(tmp_lst)
print(maxlen)