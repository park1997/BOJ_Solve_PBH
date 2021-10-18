N,M = map(int,input().split())
data = [list(map(int,input().split())) for i in range(N)]
dp = [[0]*M]*N
if N ==1:
    print(data[-1][-1])
else:
    for i in range(0,N):
        dp[0] = data[0]
        for j in range(M):
            if j==0:
                dp[i][j] = dp[i-1][j]+data[i][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+data[i][j]
    print(dp[-1][-1])