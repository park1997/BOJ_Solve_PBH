import sys
from collections import deque

def diffusion(x,y):
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    temp = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and ny>=0 and nx<R and ny<C and new_graph[nx][ny] != -1:
            temp.append([nx,ny])
    new_graph[x][y] += graph[x][y] - (graph[x][y]//5)*len(temp)
    for t in temp:
        x1,y1 = t
        new_graph[x1][y1] += graph[x][y]//5


    return
R,C,T = map(int,sys.stdin.readline().split())
graph = []
cleaner = []
for i in range(R):
    g = list(map(int,sys.stdin.readline().split()))
    for j in range(C):
        if g[j] == -1:
            cleaner.append([i,j])
    graph.append(g)
dx = [0,1,-1,0]
dy = [1,0,0,-1]


for time in range(T):
    new_graph = [[0]*C for _ in range(R)]
    for c in cleaner:
        new_graph[c[0]][c[1]] = -1
    # 먼지 확산
    for i in range(R):
        for j in range(C):
            if graph[i][j] not in [-1,0]:
                diffusion(i,j)
    # 공기 청정기 작동
    # 위
    x1,y1 = cleaner[0]
    for r1 in [2,0,1,3]:
        while 1:
            x1 += dx[r1]
            y1 += dy[r1]
            if x1<0 or y1<0 or x1>cleaner[0][0] or y1>=C :
                x1 -= dx[r1]
                y1 -= dy[r1]
                break
            if [x1,y1] == cleaner[0]:
                break
            if new_graph[x1-dx[r1]][y1-dy[r1]] == -1:
                new_graph[x1][y1] = 0
                continue
            temp = new_graph[x1][y1]
            new_graph[x1][y1] = 0
            new_graph[x1-dx[r1]][y1-dy[r1]] = temp
        
    # 아래 공기 청정기
    x2,y2 = cleaner[1]
    for r2 in [1,0,2,3]:
        while 1:
            x2 += dx[r2]
            y2 += dy[r2]
            if x2<cleaner[1][0] or y2<0 or x2>=R or y2>=C:
                x2 -= dx[r2]
                y2 -= dy[r2]
                break
            if [x2,y2] == cleaner[1]:
                break
            if new_graph[x2-dx[r2]][y2-dy[r2]] == -1:
                new_graph[x2][y2] = 0
                continue
            temp = new_graph[x2][y2]
            new_graph[x2][y2] = 0
            new_graph[x2-dx[r2]][y2-dy[r2]] = temp
        

    
    graph = [g[:] for g in new_graph]

result = 0
for g in graph:
    result += sum(g)
print(result+2)





