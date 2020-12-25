import sys
a,b=map(int,sys.stdin.readline().split())
c=list(map(int,sys.stdin.readline().split()))
real=[c[0]]
for i in range(len(c)):
    if c[i-1]==c[i]:
        continue
    else:
        real.append(c[i])
del real[0]
print(real)
