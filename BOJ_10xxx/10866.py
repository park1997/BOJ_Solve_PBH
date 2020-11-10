#덱
from collections import deque
import sys
a=int(sys.stdin.readline())
dq=deque()
for i in range(a):
    b=list(map(str,sys.stdin.readline().split()))
    if b[0]=='push_front':
        dq.appendleft(b[1])
    elif b[0]=='push_back':
        dq.append(b[1])
    elif b[0]=='pop_front':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[0])
            dq.popleft()
    elif b[0]=='pop_back':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1])
            dq.pop()
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
    elif b[0]=='back':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[-1])
