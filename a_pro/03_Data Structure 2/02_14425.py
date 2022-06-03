# python in 연산자 버전 -> 시간초과 / set 자료형 사용
import sys
n, m = map(int, sys.stdin.readline().split())
s = set()
cnt = 0
for _ in range(n):
    s.add(sys.stdin.readline().split()[0])
for _ in range(m):
    temp = sys.stdin.readline().split()[0]
    if temp in s:
        cnt += 1
print(cnt)