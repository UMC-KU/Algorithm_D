result1 = 0
result2 = 0

num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)
if(num1<num2):
    a = num1
    b = num2
else:
    a = num2
    b = num1
for i in range(1,a+1):
    if(num1%i == 0)& (num2%i == 0):
        if(result1<i):
            result1 = i

for i in range(b,a*b+1):
    if(i%num1 == 0)& (i%num2== 0):
        result2 = i
        break
    

print(result1)
print(result2)

