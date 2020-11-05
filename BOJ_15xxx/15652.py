from itertools import combinations_with_replacement
a,b=map(int,input().split())
for i in list(combinations_with_replacement([i for i in range(1,a+1)],b)):
    print(*i)
