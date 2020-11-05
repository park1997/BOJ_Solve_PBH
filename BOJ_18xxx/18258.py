#큐 2
from collections import deque
import sys
a=int(sys.stdin.readline())
dq=deque()
for i in range(a):
    b=list(map(str,sys.stdin.readline().split()))
    if b[0]=='push':
        dq.append(b[1])
    elif b[0]=='pop':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[0])
            dq.popleft()
    elif b[0]=='size':
        print(len(dq))
    elif b[0]=='empty':
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif b[0]=='front':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[0])
    else:
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1])
