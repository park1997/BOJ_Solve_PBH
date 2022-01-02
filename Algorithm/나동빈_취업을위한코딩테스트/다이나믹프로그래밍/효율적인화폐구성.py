N,M = map(int,input().split())
value = [int(input()) for i in range(N)]
value.sort()
INF = int(1e9)
dp = [INF]*(M+1)
for i in range(M+1):
    for v in value:
        if i<v:
            break
        elif i==v:
            dp[i]=1
        dp[i] = min(dp[i-v]+1,dp[i])
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])