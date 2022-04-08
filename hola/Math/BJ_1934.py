n = int(input())
result = []

for i in range (1,n+1): 
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    if(num1<num2):
        a = num1
        b = num2
    else:
        a = num2
        b = num1
    for i in range(b,a*b+1):
        if(i%num1 == 0)& (i%num2== 0):
            result.append(i)
            break
    
for i in range(0,len(result)):
    print(result[i])

