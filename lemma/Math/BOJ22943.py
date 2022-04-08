# # 수
#
# import sys
# from math import sqrt
#
#
# def is_prime_number(x):
#     if x == 0 or x == 1:
#         return False
#     for i in range(2, int(sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True
#
#
# min_num = '10234'
# max_num = '98765'
#
# K, M = map(int, sys.stdin.readline().split())
# min_num = int(min_num[:K])
# max_num = int(max_num[:K])
#
# # 1. 서로 다른 두 개의 소수의 합으로 나타낼 수 있는 경우
# list_1 = []
# for i in range(min_num, max_num + 1):
#     for j in range(min_num + 1, max_num + 1):
#         if is_prime_number(i) and is_prime_number(M-i) and i != M:
#             pass
#
#
# # 2. M으로 나누어 떨이지지 않을 때까지 나눈 수가 두 개의 소수의 곱인 경우 (두 소수가 같아도 됨)
# list_2 = []
#
# # 0~9 K가지의 숫자를 한 번씩만 사용하여 만들 수 있는 수인가?
