'''
7
15 11 4 8 5 2 4 
'''
N = int(input())
s = list(map(int,input().split()))
s = list(reversed(s))
dp = [1]*N
for i in range(1,len(s)):
    for j in range(i):
        if s[i]>s[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(N-max(dp))


