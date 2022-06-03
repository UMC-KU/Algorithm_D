# 1부터 n까지의 원순열에서 매번 k번째 수를 제거하는 요세푸스 수열을 출력하는 프로그램
n, k = map(int, input().split())
lst = [i for i in range(1, n+1)]
p = []
index = (k-1) % len(lst)
for i in range(n):
    p.append(lst.pop(index))
    index += k - 1
    if len(lst) > 0:
        index %= len(lst)
print('<', end = '')
for i, element in enumerate(p):
    if i == len(p) - 1:
        print('%d>' % element)
    else:
        print('%d, ' % element, end = '')
