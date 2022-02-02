import sys
from collections import deque
s = deque()
while 1:
    o = list(map(str,sys.stdin.readline().split()))
    if o[0] =='push':
        print(o[1])
        s.append(o[1])
    elif o[0] =='pop':
        if len(s)!=0:
            print(s.pop())
        else:
            print(-1)
    elif o[0] =='size':
        print(len(s))
    elif o[0] =='empty':
        if len(s)==0:
            print(1)
        else:
            print(0)
    elif o[0] == "top":
        if len(s)==0:
            print(-1)
        else:
            print(s[-1])
    elif o[0] == "end":
        break
