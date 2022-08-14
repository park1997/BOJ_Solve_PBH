# 보물섬
import sys
from collections import deque
def bfs(x,y):
    global graph,N,M
    t_graph = [g[:] for g in graph]
    visited = [[False]*M for _ in range(N)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    q = deque()
    q.append([x,y])
    visited[x][y] = True
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<M:
                if t_graph[nx][ny] == 0 and not visited[nx][ny]:
                    t_graph[nx][ny] = t_graph[a][b] + 1
                    visited[nx][ny] = True
                    q.append([nx,ny])
    t_max = -1
    for t in t_graph:
        if t_max < max(t):
            t_max = max(t)
    return t_max

N,M = map(int,sys.stdin.readline().split())
graph = [list(map(str,sys.stdin.readline().strip())) for _ in range(N)]

for x in range(N):
    for y in range(M):
        if graph[x][y] == "L":
            graph[x][y] = 0
        elif graph[x][y] == "W":
            graph[x][y] = -1

result = -1
for x in range(N):
    for y in range(M):
        if graph[x][y] == 0:
            temp = bfs(x,y)
            if result < temp:
                result = temp
print(result)