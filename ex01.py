# 40분 걸린 문제
import sys
def vivaragi(d,s,groom):
    global graph, N
    dx = [0,-1,-1,-1,0,1,1,1]
    dy = [-1,-1,0,1,1,1,0,-1]
    visited = [[False]*N for _ in range(N)]
    new_groom = []
    for g in groom:
        gx, gy = g
        gx = gx + dx[d] * s
        gy = gy + dy[d] * s
        gx = gx % N
        gy = gy % N
        new_groom.append([gx,gy])
        graph[gx][gy] += 1
        visited[gx][gy] = True

    for ng in new_groom:
        ngx, ngy = ng
        for direc in [1,3,5,7]:
            nx = ngx + dx[direc]
            ny = ngy + dy[direc]
            if nx>=0 and ny>=0 and nx<N and ny<N and graph[nx][ny] > 0:
                graph[ngx][ngy] += 1
                if graph[nx][ny] < 2:
                    visited[nx][ny] = True
    next_groom = []
    for x in range(N):
        for y in range(N):
            if  not visited[x][y] and graph[x][y] >= 2:
                next_groom.append([x,y])
                graph[x][y] -= 2

    return next_groom

N, M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
groom = []
for i in range(M):
    if i == 0:
        groom = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
    d,s = map(int,sys.stdin.readline().split())
    groom = vivaragi(d-1,s,groom)

result = 0
for g in graph:
    result += sum(g)
print(result)
