N,M = map(int,input().split())
data = [list(map(int,input().split())) for i in range(N)]
dp = [[0]*(M+1)]*(N+1)
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = max(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+data[i-1][j-1]
print(dp[-1][-1])