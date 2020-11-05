#ATM
import sys
a=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))
b.sort()
num=0
for i in range(a):
    num+=sum(b[:i+1])
print(num)
