# 규칙 :
# 1. 맨 위의 카드 한 장을 버린다
# 2. 맨 위의 카드 한 장을 맨 밑으로 집어넣는다
# 이를 반복해 마지막에 남은 카드 한 장을 출력하는 프로그램
from collections import deque
n = int(input())
cards = deque([i for i in range(1, n+1)])
while len(cards) > 1:
    cards.popleft()
    #cards.rotate(-1)
    cards.append(cards.popleft())   # 위에서 한 장 빼서 오른쪽에 집어넣는 코드
print(cards[0])