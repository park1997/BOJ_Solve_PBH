# 퇴사
a=int(input())
num=[list(map(int,input().split())) for i in range(a)]
result=[0]*a
for i in range(a):
    if num[i][0]+i<=a:
        result[i]=num[i][1]
        for j in range(i):
            if j+num[j][0]<=i:
                result[i]=max(result[i],result[j]+num[i][1])
print(max(result))