# 레이져로 쇠 막대를 잘랐을 때 몇개가 나오는지 구하는 프로그램.
# x방향으로 한칸씩 움직였을 때 stick 새로 나오면 stick_number 증가
# 레이져로 자르면 기존 stick_number만큼 잘려진 막대 생성
# 막대 끝나면 개수 +1 stick_number -1
line = input()
n = len(line)
i = 0
stick_number = 0
split = 0
while i < n:
    if i < n-1 and line[i] + line[i+1] == '()':
        # 레이져일 경우
        split += stick_number
        i += 1
    elif line[i] == '(':
        # 막대 하나 추가
        stick_number += 1
    elif line[i] == ')':
        # 막대 하나 끝
        stick_number -= 1
        split += 1
    i += 1
print(split)