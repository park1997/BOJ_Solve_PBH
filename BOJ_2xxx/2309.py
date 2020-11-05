from itertools import combinations
a=[int(input()) for i in range(9)]
b=[]
for i in list(combinations(a,7)):
    if sum(i)==100:
        for j in i:
            b.append(j)
        b.sort()
        for k in b:
            print(k)
        break
