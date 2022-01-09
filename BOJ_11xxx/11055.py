# 가장 큰 증가 부분 수열
a=int(input())
b=list(map(int,input().split()))
dp=[0]*a
dp[0]=b[0]
for i in range(1,a):
    for j in range(i):
        if b[i]>b[j]:
            dp[i]=max(dp[i],dp[j]+b[i])
    if dp[i]==0:
        dp[i]=b[i]
print(max(dp))