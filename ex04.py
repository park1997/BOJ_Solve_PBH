from collections import deque
import sys

V,E = map(int,input().split())
K = int(input())
graph = [list(map(int,input().split())) for _ in range(E)]
graph = []
start = []
for _ in range(E):
    a = list(map(int,input().split()))
    graph.append(a)
    if a[0]==K:
        start.append(a)
print(graph)

INF = int(1e9)
node = [INF]*(V+1)
visited = [False]*(V+1)
node[K] = 0
visited[K] = True

q = deque(start)
while q:
    u,v,w = q.popleft()
    visited[u] = True
    for g in graph:
        if g[0] == u and not visited[v]:
            node = min(node[v],node[u]+w)
        
