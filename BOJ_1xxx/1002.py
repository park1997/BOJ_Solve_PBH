#터렛
import math
import sys
a=int(sys.stdin.readline())
for i in range(a):
    x1,y1,r1,x2,y2,r2=map(float,sys.stdin.readline().split())
    d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
        else:
            print(0)
        continue
    if r1 > d + r2 or r2 > d + r1 or d > r1 + r2:
        print(0)
    elif r1 == d + r2 or r2 == d + r1 or r1 + r2 == d:
        print(1)
    else:
        print(2)
