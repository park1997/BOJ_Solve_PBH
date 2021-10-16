N = int(input())
if N ==1:
    print(9)
else:
    dp = {}
    for i in range(10):
        dp[i]=0
    for i in range(1,N):
        for j in dp:
            if j==0:
                dp[1]+=1
            elif j==9:
                dp[8]+=1
            else:
                dp[j-1]+=1
                dp[j+1]+=1
        if i ==1:
            dp[0] = 0
        print(dp)