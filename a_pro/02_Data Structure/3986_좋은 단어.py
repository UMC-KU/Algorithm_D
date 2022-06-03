# 들어온 단어가 '좋은 단어'인지 판별하는 프로그램
# 스택에 단어 각각을 담아뒀다가 같은 단어가 오면 그 단어를 뺌.
# 마지막에 스택이 남아 있지 않으면 '좋은 단어'인것.
# 자료구조인데 생각하지 좀 어려운것 -> 스택.
import sys
from collections import deque
cnt = 0 # 개수 세주는 변수
n = int(input())

for _ in range(n):
    stack = deque()
    # 입력받는 부분
    word = sys.stdin.readline().rstrip()
    for i in word:
        if not stack or stack[0] != i:  # 스택에 값이 없거나 첫 값이 i와 다른 경우
            stack.appendleft(i)
        else:                           # 그 경우를 제외한 다른 경우는 값이 있고 i와 첫값이 같은 경우밖에 없음.
            stack.popleft()
    # 값이 없으면 성공.
    if not stack:
        cnt += 1
print(cnt)