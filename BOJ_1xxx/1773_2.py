# 폭죽쇼
import sys
a,b=map(int,sys.stdin.readline().split())
result=[0]*(b+1)
for i in range(a):
    c=int(sys.stdin.readline())
    for j in range(c,b+1,c):
        result[j]=1
print(sum(result))