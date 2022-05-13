import sys
from collections import deque
def bfs(start):
    global population
    visited[start[0]][start[1]] = True
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque([start])
    union = []
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<N and not visited[nx][ny]:
                if L<= abs(graph[a][b]-graph[nx][ny])<=R:
                    q.append([nx,ny])
                    union.append([nx,ny])
                    visited[nx][ny] = True
                    visited[a][b] = True
                    if [a,b] not in union:
                        union.append([a,b])

    if len(union) != 0:
        population.append(union)

N,L,R = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
day = 0
while 1:
    
    population = []
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            bfs([i,j])
            
    if len(population) ==0:
        print(day)
        break
    else:
        for p in population:
            mean = 0
            for u in p:
                mean += graph[u[0]][u[1]]
            mean = mean // len(p)
            for u in p:
                graph[u[0]][u[1]] = mean
    day += 1
    for g in graph:
        print(g)
    print()



