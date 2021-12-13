# 예산
import sys
a=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))
c=int(sys.stdin.readline())
x=0
y=max(b)
while x<=y:
    mid=(x+y)//2
    whole=0
    for i in b:
        whole+=min(mid,i)
    if whole<=c:
        x=mid+1
    elif whole>c:
        y=mid-1
print(y)
