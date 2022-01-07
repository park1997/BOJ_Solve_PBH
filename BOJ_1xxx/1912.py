# 연속합
a=int(input())
b=list(map(int,input().split()))
if a==1:
    print(b[0])
elif a==2:
    print(max(b[1],b[0]+b[1]))
else:
    dp=[0]*a
    dp[0]=b[0]
    dp[1]=max(b[1],b[0]+b[1])
    dp[2]=max(dp[1]+b[2],b[2])
    for i in range(3,a):
        dp[i]=max(dp[i-1]+b[i],b[i])
    print(max(dp))