import sys
n = int(sys.stdin.readline())
dp = [int(1e9)] *(n+1)
dp[1] = 1
for i in range(1,n):
    if i**2<=n:
        dp[i**2] = 1
for i in range(1,n+1):
    if dp[i] == 1:
        continue
    for j in range(1,i+1):
        if i-j**2>=0:
            dp[i] = min(dp[i],dp[i-j**2]+dp[j**2])
        else:
            break
print(dp)
print(dp[-1])