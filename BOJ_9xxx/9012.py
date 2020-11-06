#괄호
import sys
from collections import deque
a=int(sys.stdin.readline())
for i in range(a):
    dq=deque(str(input()))
    while len(dq)!=0:
        if dq.count('(') != dq.count(')'):
            print('NO')
            break
        if '(' in dq and ')' in dq:
            if dq.index('(') > dq.index(')'):
                print('NO')
                break
            else:
                dq.remove('(')
                dq.remove(')')
        else:
            print('NO')
            break
        if len(dq)==0:
            print('YES')
            break
