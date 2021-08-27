# 킹, 퀸, 룩, 비숍, 나이트, 폰
num=[1,1,2,2,2,8]
a=list(map(int,input().split()))
result=[]
for i in range(6):
    result.append(num[i]-a[i])
print(*result)