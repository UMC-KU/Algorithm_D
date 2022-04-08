from collections import Counter

n = int(input())
list=[]

for i in range (n):
    string = input()
    result = Counter(string)
    r = result.most_common(2)
    if r[0][1]==r[1][1]:
        list.append("?")
    else:
        list.append(r[0][0])

for j in range (len(list)):
    print(list[j])

