# 2504 => hard...
# 재귀함수로 간신히 구현
from collections import deque
line = input()
shape = {
    '(':')',
    '[':']'
}
succeed = 1
def case(index):
    global succeed
    # succeed = 0이면 바로 0 반환하며 종료
    if succeed == 0:
        return 0
    
    res = 0
    queue = deque()  # 같은 레벨의 괄호 시작 지점 저장
    # 시작점 찾아 저장하는 부분
    if line[index] in '([':
        tmp = index
        level = 0
        while tmp < len(line) and level >= 0:  # 끝까지 가면서 같은 레벨의 시작지점 찾아 queue에 저장
            if level == 0 and line[tmp] in '([':
                queue.append(tmp)
            
            if line[tmp] in '([':
                level += 1
            else:
                level -= 1
            
            tmp += 1

    # queue에서 값을 하나씩 빼면서 진행
    while queue:
        temp = queue.popleft()
        ch = line[temp]             # 시작하는 괄호 종류 저장
        if temp < len(line) - 1:    # 마지막이 아닐 때
            if line[temp+1] == shape[ch]:           # 이번이 최소 단위이면
                res += '__(['.index(line[temp])
            elif line[temp + 1] in '([':            # 안에 괄호가 또 있다면
                if queue and shape[ch] != line[queue[0]-1]: # 괄호 끝날 때 값이 시작시 값과 다르다면 틀린 것.
                    succeed = 0
                    return 0
                res += '__(['.index(line[temp]) * case(temp+1)
            else:                                   # 정상적이지 않은 경우라면
                succeed = 0
                return 0
    return res

# 간단하게 오류 검사, 짝을 지어 있어야 하므로 둘이 개수 다르면 틀린 것.
if line.count('(') + line.count('[') != line.count(')') + line.count(']'):  # 간단하게 검사
    succeed = 0
# 이부분 추가해주니까 성공함!!!!
if line.count('(') != line.count(')'):
    succeed = 0

# 결괏값 임시 저장
result = case(0)

# 마지막 출력 부분, 오류 있으면 0 출력
if succeed:
    print(result)
else:
    print(0)