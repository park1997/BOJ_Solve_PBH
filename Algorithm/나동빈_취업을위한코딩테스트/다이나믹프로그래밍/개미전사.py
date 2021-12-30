'''
4
1 3 1 5
8

6
1 3 1 5 6 4
'''
N = int(input())
s = list(map(int,input().split()))
dp = [0]*N
dp[0] = s[0]
dp[1] = s[1]
for i in range(2,N):
    dp[i] = max(dp[i-1],dp[i-2]+s[i])
print(dp[-1])
