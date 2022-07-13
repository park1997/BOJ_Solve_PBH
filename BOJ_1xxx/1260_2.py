# DFS와 BFS
from collections import deque
import sys
N,M,V = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for j in range(1,N+1):
    graph[j].sort()

def bfs(start):
    # global visited
    q = deque([start])
    while q:
        s = q.popleft()
        print(s,end=" ")
        visited[s] = True
        for i in graph[s]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


def dfs(start):
    # global visited
    visited[start] = True
    print(start,end = " ")
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

visited = [False]*(N+1)
dfs(V)
print()
visited = [False]*(N+1)
bfs(V)