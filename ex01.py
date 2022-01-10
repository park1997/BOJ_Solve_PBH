import sys
N = int(sys.stdin.readline())
num = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [0]*(N)
for i in range(N):
    if num[i][0] + i <= N:
        dp[i] = num[i][1]
        for j in range(i):
            if i >= j + num[j][0]:
                dp[i] = max(dp[j],num[i][1]+dp[j])
    else:
        dp[i] = 0
        for j in range(i):
            if i >= j+num[j][0]:
                dp[i] = max(dp[j],dp[i])
print(max(dp))
print(dp)