from itertools import product
a,b=map(int,input().split())
for i in list(product([i for i in range(1,a+1)],repeat = b)):
    print(*i)
