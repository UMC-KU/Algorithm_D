from math import sqrt


def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    for j in range(2, int(sqrt(x)) + 1):
        if x % j == 0:
            return False
    return True


N = input()

while True:
    num = int(len(N) / 2)
    count = 0
    for i in range(num):
        if N[i] == N[-i - 1]:
            count += 1
    if num == count and is_prime_number(int(N)):
        print(N)
        break
    else:
        N = str(int(N) + 1)
