# 리스트 이용해 푼 문제

import sys
n, m = map(int, sys.stdin.readline().split())
book = []
for i in range(n):
    book.append(sys.stdin.readline().split()[0])

for i in range(m):
    question = sys.stdin.readline().split()[0]
    if question[0] in '0123456789':             # 숫자로만 이루어져 있다는 점 이용
        question = int(question)
        print(book[question - 1])
    else:
        print(book.index(question) + 1)
"""
# 딕셔너리 버전
import sys
n, m = map(int, sys.stdin.readline().split())
book = dict()
for i in range(n):
    book[sys.stdin.readline().split()[0]] = i

for i in range(m):
    question = sys.stdin.readline().split()[0]
    if question[0] in '0123456789':             # 숫자로만 이루어져 있다는 점 이용
        question = int(question)
        for j in book.items():
            if j[1] + 1 == question:
                print(j[0])
                break

    else:
        print(book[question] + 1)
"""