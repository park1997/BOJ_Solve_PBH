#1,2,3 더하기 3
import sys
a=int(sys.stdin.readline())
r=[0]*1000001
r[0]=1
r[1]=2
r[2]=4
for i in range(3,1000001):
    r[i]=(r[i-1]+r[i-2]+r[i-3])%1000000009
for i in range(a):
    b=int(input())
    print(r[b-1])
