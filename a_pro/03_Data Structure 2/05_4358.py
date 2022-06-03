# 나무 종류 입력받고 그 비율 출력하는 프로그램
# EOF 에러 때문에 고생함. 입력이 없을 때 break하는 식으로 종료.
import sys
names = dict()
total = 0
while True:
    wood = sys.stdin.readline().rstrip()
    if not wood:
        break
    total += 1
    # 각 항목이 있으면 1추가, 없으면 1로 설정(추가)
    if wood in names:
        names[wood] += 1
    else:
        names[wood] = 1

woods = sorted(names.keys())    # 정렬된 이름 리스트
for element in woods:
    print(element, '%.4f' % (names[element] / total * 100))