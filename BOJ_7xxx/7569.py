# 토마토
from collections import deque
import sys
M,N,H = map(int,sys.stdin.readline().split())
graph = []
for i in range(H):
    t = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    graph.append(t)
t = []
for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 1:
                t.append([z,y,x])
# bfs 수행
q = deque()
for i in t:
    q.append(i)
while q:
    c,b,a = q.popleft()
    dx = [0,1,0,-1,0,0]
    dy = [1,0,-1,0,0,0]
    dz = [0,0,0,0,1,-1]
    for i in range(6):
        nx = a + dx[i]
        ny = b + dy[i]
        nz = c + dz[i]
        if nx>=0 and ny>=0 and nz >=0 and nx<M and ny<N and nz<H:
            if graph[nz][ny][nx]==0:
                graph[nz][ny][nx] = graph[c][b][a] + 1 
                q.append([nz,ny,nx])
flag = True
for i in graph:
    for j in i:
        if 0 in j:
            flag = False
            break

result = -2
if flag:
    for i in graph:
        for j in i:
            if result < max(j):
                result = max(j)
    print(result-1)
else:
    print(-1)