# 16953 : a -> B
# a를 b로 만들기 위해 최소 몇 번의 연산이 필요한지 출력하는 프로그램
# 1. *2
# 2. *10 + 1
# 만들 수 없다면 -1 출력
# solved
a, b = map(int, input().split())
def step(n):
    global lst
    if n * 2 <= b and (n*2 not in lst or lst[n*2] > lst[n] + 1):
        lst[n*2] = lst[n] + 1
        step(n*2)
    if n * 10 + 1 <= b and (n*10+1 not in lst or lst[n*10+1] > lst[n] + 1):
        lst[n*10+1] = lst[n] + 1
        step(n*10+1)
    return
lst = dict()
lst[a] = 1
i = a
step(a)
if b in lst:
    print(lst[b])
else:
    print(-1)

"""
lst = [0] * (b + 1)
lst[a] = 1
for i in range(a, b + 1):
    if lst[i] and i * 2 <= b and (not lst[i*2] or lst[i*2] > lst[i] + 1):
        lst[i*2] = lst[i] + 1
    if lst[i] and i * 10 + 1 <= b and (not lst[i*10 + 1] or lst[i*10 + 1] > lst[i] + 1):
        lst[i*10 + 1] = lst[i] + 1
if(not lst[b]):
    print(-1)
else:
    print(lst[b])
"""