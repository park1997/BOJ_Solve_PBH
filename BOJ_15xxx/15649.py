from itertools import permutations
a,b=map(int,input().split())
for i in list(map(" ".join,permutations([str(i) for i in range(1,a+1)],b))):
    print(i)
