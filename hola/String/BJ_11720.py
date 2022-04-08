n = int(input())
num = input()
list = list(num)
result =0
for i in range (0,n):
    list[i] = int (list[i])
    result += list[i]

print(result)
