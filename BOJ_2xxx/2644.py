# 촌수 계산
import sys
from collections import deque
def bfs(start):
    global graph, visited, count
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        s = q.popleft()
        for i in graph[s]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                count[i] = count[s] + 1
n = int(sys.stdin.readline())
c1,c2 = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(n+1)
count = [0]*(n+1)
bfs(c1)
if count[c2]==0:
    print(-1)
else:
    print(count[c2])