A,B,C,M = input().split()
A = int(A)
B = int(B)
C = int(C)
M = int(M)

p = 0
b = 0

if(A>M):
    print(p)
else:
    for i in range(1,25):
        if(p+A<=M):
            p+=A
            b+=B
        else:
            if(p-C>=0):
                p-=C
            else:
                p=0
    print(b)