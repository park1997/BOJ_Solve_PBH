# 나무자르기
#이분탐색
a,b=map(int,input().split())
c=list(map(int,input().split()))
num1=1
num2=max(c)
while num1<=num2:
    count=0
    mid=(num1+num2)//2
    for i in c:
        if i>mid:
            count+=i-mid
    if b<=count:
        num1=mid+1
    else:
        num2=mid-1
print(num2)
