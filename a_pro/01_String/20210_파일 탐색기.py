# 어렵...
import sys
from collections import deque
"""
mapping = dict(zip((), ''))
def convert(n, MAX):
    res = []
    n = deque(n)
    temp = ''
    length = len(n)
    for i in range(length):
        if ord('a') <= ord(n[0]) <= ord('z') or ord('A') <= ord(n[0]) <= ord('Z'):
            if temp:
                res.append(temp)
                temp = ''
            res.append(n.popleft())
        else:
            temp += n.popleft()
    return res

n = int(input())
words = []
sort_lst = [[] * (52 + 10)]
sort_lst_save = [[] * (52 + 10)]
MAXLEN = 0  # 가장 긴 단어의 길이 저장
for _ in range(n):
    words.append(sys.stdin.readline().strip('\n'))
    if len(words[-1]) > MAXLEN:
        MAXLEN = len(words[-1])

for i in range(len(words)):
    words[i] = convert(words[i], MAXLEN)
for i in words:
    print(i)
"""

words = []
index = []
words_index = dict()
upper = [chr(i) for i in range(ord('A'), ord('A')+26)]
lower = [chr(i) for i in range(ord('a'), ord('a')+26)]
numeric_value = '0123456789'
value = numeric_value
for i in range(26):
    value += upper[i]
    value += lower[i]


n = int(input())
for _ in range(n):
    words.append(sys.stdin.readline().strip('\n'))
    index.append([words[-1][0]])
    i = 1
    while i < len(words[-1]):
        if words[-1][i] in numeric_value and words[-1][i-1] in numeric_value or words[-1][i] not in numeric_value and words[-1][i-1] not in numeric_value :
            index[-1].append(words[-1][i])
        else:
            
        i += 1