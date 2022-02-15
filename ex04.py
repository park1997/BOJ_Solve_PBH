import sys
x,N = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
dp = [0]*(N+1)
m = int(1e9 + 7)
for n in nums:
    dp[n] = 1
for i in range(N+1):
    for n in nums:
        if i-n>=0:
            dp[i] += dp[i-n]%m
print(dp[N]%(m))