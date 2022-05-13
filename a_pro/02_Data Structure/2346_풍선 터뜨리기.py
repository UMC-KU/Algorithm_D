# 원형으로 둘러싼 풍선들을 터뜨리는 순서를 출력하는 프로그램
# 처음엔 1번재 풍선을, 다음부턴 풍선 속의 번호를 보고 그 다음 번째 풍선을 터뜨림.
# 
import sys
n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))  # 각 풍선에 있는 번호들
lst = []
balloons = [i for i in range(1, n+1)]   # 풍선들
index = 0

for _ in range(n):
    temp = balloons.pop(index)  # temp는 현재 터트린 풍선의 번호값
    lst.append(temp)            # lst 에 저장
    move = numbers[temp-1]      # move는 numbers에 저장된 풍선 속 번호
    index += move               # move만큼 index값 변화시켜줌
    if move > 0:                # 단, 풍선이 터져서 pop되었으므로 그 뒤의 풍선이 한칸씩 밀렸으므로 move가 1일때는 움직여줄 필요가 없음. 따라서 move값이 양수이면 1 빼줌.
        index -= 1
    if len(balloons) > 0:       # balloons에 값이 남아 있지 않을 수 있음.
        index %= len(balloons)

for i in lst:
    print(i, end = ' ')