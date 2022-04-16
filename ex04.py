import sys
from collections import deque


N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
indgree = [0]*(N+1)
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indgree[b] += 1
q = deque()
for i in range(1,N+1):
    if indgree[i] == 0:
        q.append(i)

while q:
    a = q.popleft()
    for i in graph[a]:
        indgree[i] -= 1
        if indgree[i] == 0:
            q.append(i)
    print(a,end=" ")





