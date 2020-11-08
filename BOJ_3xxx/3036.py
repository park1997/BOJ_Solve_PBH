#링
import math
import sys
i=sys.stdin.readline
a=int(i())
b=list(map(int,i().split()))
for i in range(a-1):
    print("{}/{}".format(b[0]//math.gcd(b[0],b[i+1]),b[i+1]//math.gcd(b[0],b[i+1])))
