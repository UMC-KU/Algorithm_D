n = int(input())
result=n
count =0

while True:
    result = (result%10*10)+(result//10+result%10)%10

    count+=1
    if(result == n):
        break

print(count)
    