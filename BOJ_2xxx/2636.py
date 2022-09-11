# 치즈
import sys
from collections import deque

def bfs(s):
    global visited, graph, c
    q = deque(s)
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    temp_c =[]
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<M:
                if not visited[nx][ny] and graph[nx][ny]==0:
                    q.append([nx,ny])
                    visited[nx][ny] = True
                if not visited[nx][ny] and graph[nx][ny]==1:
                    temp_c.append([nx,ny])
                    visited[nx][ny] = True
                    graph[nx][ny] = 0
    c = temp_c
    result.append(len(c))

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

visited = [[False]*(M) for _ in range(N)]
c = [[0,0]]
result = []
day = -1
while 1:
    day += 1
    bfs(c)
    if len(c)==0:
        break
print(day)
print(result[-2])