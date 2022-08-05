# 1990 - 소수 인 팰린드롬
# a이상 b 이하인 소수인 팰린드롬을 모두 구하는 프로그램
import time


def palindrome(n):
    word = str(n)
    length = len(word)
    for i in range(length//2):
        if word[i] != word[length - 1 - i]:
            return 0
    return 1


a, b = map(int, input().split())
st = time.time()
check_lst = [
    # 0, 1, 2, 3, 4, 5 ; 2, 3, 5만 미리 제거해준 리스트.
    False, False, True, True, False, True, False
] + [True, False, False, False, True, False,
     True, False, False, False, True, False,
     True, False, False, False, True, False,
     False, False, False, False, True, False,
     True, False, False, False, False, False] * (b // 30 + 1)

print('lst create', time.time() - st)
i = 6
while i <= b:
    if check_lst[i]:    # 소수가 아닐 때
        j = i * 3
        # if palindrome(i):
        # print(i)
        while j <= b:
            check_lst[j] = False
            j += i * 2
            # 굳이 하나씩 더해 줄 필요 없음. 짝수 배 한 수만큼 더해줘도 됨. -> 여전히 1분걸림...
    i += 1
i = a
# 출력 부분
# while i <= b:
#     if check_lst[i] and palindrome(i):
#        print(i)
#     i += 1
# print(-1)
print('time :', time.time() - st)
# print(check_lst)
