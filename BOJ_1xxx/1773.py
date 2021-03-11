# 폭죽쇼
import math
a,b=map(int,input().split())
result=[0]*(b+1)
for i in range(a):
    c=int(input())
    for j in range(c,b+1,c):
        result[j]=1
print(sum(result))