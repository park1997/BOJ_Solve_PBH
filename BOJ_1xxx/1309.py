# 동물원
N = int(input())
dp1 = 1
dp2 = 1
dp3 = 1
if N==1:
    print(3)
else:
    for i in range(1,N):
        temp1 = dp1+dp2+dp3 
        temp2 = dp1+dp3
        temp3 = dp1+dp2
        dp1,dp2,dp3=temp1,temp2,temp3
    print((dp1+dp2+dp3)%9901)