# 가장 긴 증가하는 부분 수열
import sys
a=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))
result=[1]*a
for i in range(1,a):
    for j in range(i):
        if b[i]>b[j]:
            result[i]=max(result[i],result[j]+1)
print(max(result))