import sys
a=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))
c=list(map(int,sys.stdin.readline().split()))
b.sort()
c.sort()
a_sum=0
for i in range(a):
    a_sum+=b[i]*c[-i-1]
print(a_sum)
