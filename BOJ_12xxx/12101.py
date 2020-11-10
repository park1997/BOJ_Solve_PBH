#1,2,3 더하기 2
import itertools
a,b=map(int,input().split())
d=[]
for j in range(1,a+1):
    c=list(itertools.product(range(1,4), repeat = j))
    for i in c:
        if sum(i)==a:
            d.append(i)
d.sort()
if len(d)<b:
    print(-1)
else:
    print(*d[b-1],sep="+")
