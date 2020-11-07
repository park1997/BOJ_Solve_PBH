#평범한 배낭
#Knapsack dp 알고리즘이 아니면 풀수가 없다.
#굉장히 어려웠고 꼭 다시 봐야한다 생각한다.
import sys
a,b=map(int,sys.stdin.readline().split())
dp=[[0]*(b+1) for i in range(a+1)]
for i in range(1,a+1):
    w,v=map(int,sys.stdin.readline().split())
    for j in range(1,b+1):
        if j>=w:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+v)
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])
