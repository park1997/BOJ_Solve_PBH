# 치킨배달
import sys
from itertools import combinations
N,M = map(int,sys.stdin.readline().split())
house = []
chicken = []
graph = []
for i in range(N):
    l = list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        if l[j]==2:
            chicken.append([i,j])
        if l[j]==1:
            house.append([i,j])
c = list(combinations(chicken,M))
result = int(1e9)
for ch in c:
    temp_sum = 0
    for h in house:
        temp_min = int(1e9)
        for i in ch:
            k = abs(i[0]-h[0]) + abs(i[1]-h[1])
            if k<temp_min:
                temp_min = k
        temp_sum+=temp_min
    if result>temp_sum:
        result = temp_sum
print(result)


