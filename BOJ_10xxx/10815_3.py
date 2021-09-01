# 숫자 카드
import sys
i=sys.stdin.readline
num1=int(i())
a=list(map(int,i().split()))
num2=int(i())
b=list(map(int,i().split()))
a.sort()
result=[]
for i in b:
    x=0
    y=len(a)-1
    while x<=y:
        mid=(x+y)//2
        if a[mid]<i:
            x=mid+1
        elif a[mid]>i:
            y=mid-1
        else:
            result.append(1)
            break
        if x>y:
            result.append(0)
print(*result)