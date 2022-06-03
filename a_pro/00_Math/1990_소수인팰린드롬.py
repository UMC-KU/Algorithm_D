import time
def palindrome(n):
    word = str(n)
    length = len(word)
    for i in range(length//2):
        if word[i] != word[-i-1]:
            return 0
    return 1
a, b = map(int, input().split())
st = time.time()
check_lst = [False] * 2 + [False, False, False, True, False, True]* ((b-1)//6 + 1)
print('lst create', time.time() - st)
for i in range(5, b+1):
    if check_lst[i]:
        #prime_lst.append(i)
        j = i
        #if palindrome(i):
            #print(i)
        while j <= b:
            check_lst[j] = False
            j += i*2        # 굳이 하나씩 더해 줄 필요 없음. 짝수 배 한 수만큼 더해줘도 됨. -> 여전히 1분걸림...
print(-1)
print('time :', time.time() - st)