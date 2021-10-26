# Defining main function 
def main(): 
    a = input()
    temp = a.split("/")[0].split()
    N = int(temp[0])
    k = int(temp[1])
    w_p = [[int(i.split()[0]),int(i.split()[1])] for i in a.split("/")[1].split(",")]
    dp=[[0]*(k+1) for i in range(N+1)]
    for i in range(1,N+1):
        w = w_p[i-1][0]
        p = w_p[i-1][1]
        for j in range(1,k+1):
            if j>=w:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-w]+p,dp[i][j-w])
            else:
                dp[i][j]=dp[i-1][j]
    print(dp[-1][-1])
    print(dp)
if __name__=="__main__": 
    main()
    