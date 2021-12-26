# 포도주 시식
a=int(input())
b=[int(input()) for i in range(a)]
dp=[0]*a
if a==1:
    print(b[0])
elif a==2:
    print(b[0]+b[1])
elif a==3:
    print(max(b[0]+b[1],b[0]+b[2],b[1]+b[2]))
else:
    dp[0]=b[0]
    dp[1]=b[0]+b[1]
    dp[2]=max(b[0]+b[1],b[0]+b[2],b[1]+b[2])
    for i in range(3,a):
        dp[i]=max(dp[i-2]+b[i],dp[i-3]+b[i-1]+b[i],dp[i-1])
    print(max(dp))