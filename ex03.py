from math import sqrt
N = int(input())
dp = [0]*(N+1)
dp[0] = 0
dp[1] = 1
for i in range(2,N+1):
    dp[i] = i
    for j in range(1,int(sqrt(i))+1):
        dp[i] = min(dp[i],dp[i-j*j]+1)
print(dp[-1])