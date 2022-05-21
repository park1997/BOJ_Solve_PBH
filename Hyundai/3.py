import sys
M,M = map(int,sys.stdin.readline().split())
A,B = map(str,sys.stdin.readline().split())
s = 0
r1 = []
while 1:
    target = B[s:s+len(A)]
    if A == target:
        r1.append([s,s+len(A)])
    s += 1
    if s + len(A) > len(B):
        break
s1 = r1[0][0]
e1 = r1[0][1]
idx = 1
r2 = 1
while 1:
    if idx == len(r1):
        break
    ts = r1[idx][0]
    te = r1[idx][1]
    if e1 > ts:
        idx += 1
    else:
        r2 += 1
        s1 = ts
        e1 = te
        idx += 1
    

print(len(r1),r2)
