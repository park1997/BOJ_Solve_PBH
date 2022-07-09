# 바이러스
from collections import deque
N = int(input())
c = int(input())
visited = [False]*(N+1)
graph=[[] for _ in range(N+1)]
for _ in range(c):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return print(sum(visited)-1)

bfs(1)