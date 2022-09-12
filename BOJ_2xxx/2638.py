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
                if visited[nx][ny]==0 and graph[nx][ny]==0:
                    q.append([nx,ny])
                    visited[nx][ny] = 1
                if (visited[nx][ny]==0 or visited[nx][ny]==2) and graph[nx][ny]==1:
                    if visited[nx][ny]==0:
                        visited[nx][ny]+=2
                    elif visited[nx][ny]==2:
                        visited[nx][ny] = 1
                        graph[nx][ny] = 0
                        temp_c.append([nx,ny])

    c = temp_c
    result.append(len(c))

N,M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

visited = [[0]*(M) for _ in range(N)]
c = [[0,0]]
result = []
day = -1
while 1:
    day += 1
    # for i in visited:
    #     print(i)
    bfs(c)
    # for i in graph:
    #     print(i)
    # print()
    if len(c)==0:
        break
print(day)
