n = int(input())

if(n==2):
    num1, num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    if(num1<num2):
        a = num1
    else:
        a = num2
    for i in range(1,a+1):
        if(num1%i == 0)& (num2%i == 0):
            print("%d"%i)
elif(n==3):
    num1,num2,num3 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    if(num1<num2)&(num1<num3):
        a = num1
    elif(num2<num1)&(num2<num3):
        a = num2
    else:
        a = num3
    for i in range(1,a+1):
        if(num1%i==0)&(num2%i == 0)&(num3%i==0):
            print("%d"%i)
