#오븐 시계
a,b=map(int,input().split())
c=int(input())
if a+1>=24 and b+c>=60:
    a=0
    a+=(b+c-60)//60
    b=(b+c)%60
elif a+1<24 and b+c>=60:
    a+=(b+c)//60
    b=(b+c)%60
elif a+1>24 and b+c<60:
    a=0
    b=(b+c)%60
elif a+1<24 and b+c<60:
    b=b+c
if a>=24:
    a=a-24
    print("{} {}".format(a,b))
else:
    print("{} {}".format(a,b))
