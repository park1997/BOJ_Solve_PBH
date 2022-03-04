import sys
import heapq
from collections import deque
def bfs(s):
    q = deque([s])
    union = []
    # visited[i][j] = True
    while q:
        a,b = q.popleft()
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if nx>=0 and ny>=0 and nx<N and ny<N and not visited[nx][ny]:
                if L<=abs(graph[nx][ny] - graph[a][b])<=R:
                    
                    if not visited[a][b]:
                        visited[a][b] = True
                        union.append([a,b])
                    
                    visited[nx][ny] = True
                    union.append([nx,ny])

                    q.append([nx,ny])
    if len(union)!=0:
        population.append(union)
N,L,R = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
day = 0
while 1:
    visited = [[False]*N for _ in range(N)]
    population = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs([i,j])

    if len(population) == 0:
        print(day)
        break
    else:
        # print(population)
        for p in population:
            mean = 0
            for u in p:
                mean += graph[u[0]][u[1]]
            mean = mean // len(p)

            for u in p:
                graph[u[0]][u[1]] = mean

    for g in graph:
        print(g)
    print()
    day += 1
    