# 계단오르기
a=int(input())
b=[int(input()) for i in range(a)]
if a==1:
    print(b[0])
elif a==2:
    print(b[0]+b[1])
else:
    dp=[0]*a
    dp[0]=b[0]
    dp[1]=b[0]+b[1]
    dp[2]=max(b[0],b[1])+b[2]
    for i in range(3,a):
        dp[i]=max(b[i-1]+dp[i-3],dp[i-2])+b[i]
    print(dp[-1])