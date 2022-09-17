# Daisy Chains in the Field
from collections import deque
import sys
def bfs(s):
    global visited, graph
    q = deque()
    q.append(s)
    while q:
        a = q.popleft()
        visited[a] = True
        for i in graph[a]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

N,M = map(int,input().split())
visited = [False]*(N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
bfs(1)
flag = True
for i in range(1,N+1):
    if not visited[i]:
        flag = False
        print(i)
    
if flag:
    print(0)