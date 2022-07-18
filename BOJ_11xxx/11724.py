# 연결요소의 개수
from collections import deque
import sys
def bfs(start):
    global visited
    global graph
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        s = q.popleft()
        for k in graph[s]:
            if not visited[k]:
                q.append(k)
                visited[k] = True


N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        cnt +=1
print(cnt)