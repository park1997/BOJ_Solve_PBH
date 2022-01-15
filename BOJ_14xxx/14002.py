# 가장 긴 증가하는 부분 수열 4
import sys
a=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))
dp=[1]*a
for i in range(1,a):
    for j in range(i):
        if b[i]>b[j]:
            dp[i]=max(dp[i],dp[j]+1)
x=max(dp)
print(x)
result=[]
for i in range(dp.index(x),-1,-1):
    if dp[i]==x:
        result.append(b[i])
        x-=1
print(*reversed(result))
