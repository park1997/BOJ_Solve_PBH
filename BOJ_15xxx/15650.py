from itertools import combinations
a,b=map(int,input().split())
for i in list(combinations(range(1,a+1),b)):
    print(*i)
