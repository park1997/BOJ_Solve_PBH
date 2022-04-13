import sys
from collections import deque
v,e = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(v+1)]
indgree = [0]*(v+1)
for _ in range(e):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indgree[b] += 1

def topology_sort():
    result = []
    q = deque()
    for idx,i in enumerate(indgree):
        if i == 0:
            q.append(idx)
    while q:
        a = q.popleft()
        result.append(a)
        for d in graph[a]:
            indgree[d] -= 1
            if indgree[d] == 0:
                q.append(d)
    return result
r = topology_sort()
print(*r)

'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''