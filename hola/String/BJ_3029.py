hour1,min1,second1 = map(int,input().split(':'))
hour2,min2,second2 = map(int,input().split(':'))

time1 = hour1*60*60 + min1*60 + second1
time2 = hour2*60*60 + min2*60 + second2

if(time1<time2):
    result = time2 - time1
else:
    result = time2+24*60*60 - time1

hour = result//60//60
min = result//60%60
second = result%60
print("%02d:%02d:%02d"%(hour,min,second))

