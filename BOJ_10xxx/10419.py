#지각
import sys
a=int(sys.stdin.readline())
t=1
for j in range(a):
    b=int(sys.stdin.readline())
    while 1:
        s=t*t
        if b-t-s>=0:
            t+=1
        else:
            print(t-1)
            t=0
            break
