#카드2
import sys
from collections import deque
dq=deque(range(1,int(sys.stdin.readline())+1))
if len(dq)==1:
    print(1)
else:
    while 1:
        dq.popleft()
        dq.append(dq[0])
        dq.popleft()
        if len(dq)==1:
            print(dq[0])
            break
