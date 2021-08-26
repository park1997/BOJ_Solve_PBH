# 백설공주와 일곱난장이
from itertools import combinations
a=[int(input()) for i in range(9)]
for i in list(combinations(a,7)):
    if sum(i)==100:
        for j in i:
            print(j)
        break
