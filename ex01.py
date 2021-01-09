a=int(input())
h=list(map(int,input().split()))
p=list(map(int,input().split()))
dp=[[0]*100 for i in range(a+1)]
for i in range(1,a+1):
    health=h[i-1]
    plesure=p[i-1]
    for j in range(1,100):
        if j<health:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],plesure+dp[i-1][j-health])
print(dp[-1][-1])
