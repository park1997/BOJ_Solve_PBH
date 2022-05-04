# 상자 넣기
n = int(input())
data = list(map(int,input().split()))
dp =[0]*n
dp[0] = 1
for i in range(1,n):
    max_ = 0
    for j in range(i):
        if data[i] > data[j]:
            if max_<dp[j]:
                max_ = dp[j]
        dp[i] = max_ +1
print(max(dp))

