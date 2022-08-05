import math

def prime(n):
    for i in range(2, n**0.5+1):
        if n % i == 0:
            return 0
    return 1

# 수가 주어졌을때 그 수보다 큰 최소 팰린드롬 리턴.
def palindrome_to_n(n):
    length = len(str(n))
    if n <= 9:
        return n
    res = 1
    nth = 2 # 숫자 자릿수, n자리수
    p_num = 9   # n번째 palidrome
    
    while n > 10 ** nth:
        nth += 1
    # 10**nth-1 < n <= 10**nth
    
    p_num += 10**(nth-1)-1
    # p_num = nth-1째 자리까지의 palidrome개수 구함.


    return

def n_to_palidrome():
    return 
