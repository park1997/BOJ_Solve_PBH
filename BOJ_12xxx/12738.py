# 가장 긴 증가하는 부분 수열 3
import sys
a=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))
result=[]
for i in range(a):
    x=0
    y=len(result)-1
    while x<=y:
        mid=(x+y)//2
        if result[mid]<b[i]:
            x=mid+1
        else:
            y=mid-1
    if x>=len(result):
        result.append(b[i])
    else:
        result[x]=b[i]
print(len(result))
