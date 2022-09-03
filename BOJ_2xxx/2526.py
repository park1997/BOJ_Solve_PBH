# 싸이클
import sys
N,P  = map(int,sys.stdin.readline().split())
r = []
n = N
cnt = 0
while 1:
    n = (n*N)%P
    if n in r:
        print(len(r) - r.index(n))
        break
    r.append(n)