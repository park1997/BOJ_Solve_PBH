n,m = map(int,input().split())
idx = max(m,n)
dp = [float('inf')]*(100001+1)
dp[n] = 0
for i in range(100001):
    t = abs(n-i)
    dp[i] = min(dp[i],t)
for i in range(n+1,100001):
    if i%2==0:
        dp[i] = min(dp[i],dp[i//2],dp[i-1]+1,dp[i+1]-1)
    else:

        dp[i] = min(dp[i],dp[i-1]+1,dp[i+1]-1)


print(dp[:m+1])
print(dp[m])