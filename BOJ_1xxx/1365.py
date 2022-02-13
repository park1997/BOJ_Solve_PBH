# 꼬인 전깃줄
import sys
a=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))
c=[]
cnt=0
for i in range(a):
    x=0
    y=len(c)-1
    while x<=y:
        mid=(x+y)//2
        if c[mid]<b[i]:
            x=mid+1
        else:
            y=mid-1
    if x>=len(c):
        c.append(b[i])
    else:
        c[x]=b[i]
        cnt+=1
print(cnt)
