# 100000 이상의 가장 작은 소수 팰린드롬은 1003001임을 이용, 
# 최대 나올 수 있는 결과가 그 수이므로 그 수만큼 공간을 만들고, 처리함
# 처음에는 리스트 크기를 2* n으로 했는데, 소수가 그 범위 안에 존재할 뿐이지
# 꼭 팰린드롬이라는 보장이 없음.
n = int(input())
lst = [0] * (1003002)
i = 2
while i <= 1003001:
    if lst[i] == 0:
        if i >= n and str(i) == str(i)[::-1]:
            print(i)
            break
        for j in range(i, 1003002, i):
            lst[j] = 1
    i += 1