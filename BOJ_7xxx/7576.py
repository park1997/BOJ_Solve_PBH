# 토마토
import sys
from collections import deque
cnt = 0
def bfs(tomato):
    global graph
    global cnt
    q = deque()
    for t in tomato:
        q.append(t)
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while q:
        # print(q)
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<M and graph[nx][ny]==0:
                q.append([nx,ny])
                cnt+=1
                graph[nx][ny] = graph[a][b]+1

M,N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
tomato = []
for x in range(N):
    for y in range(M):
        if graph[x][y] == 1:
            tomato.append([x,y])
bfs(tomato)
flag = True
result = 0
for i in graph:
    if result < max(i):
        result = max(i)
    if 0 in i:
        print(-1)
        flag = False
        break
if flag:
    print(result-1)