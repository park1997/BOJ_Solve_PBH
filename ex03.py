import sys
from collections import deque

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
graph = [[[] for _ in range(4)] for _ in range(4)]
for i in range(4):
    g = list(map(int,sys.stdin.readline().split()))
    temp = []
    for j,item in enumerate(g):
        if j % 2 == 0:
            graph[i][j//2] = [i,j//2,item]
        else:
            graph[i][j//2].append(item-1)

shark = [0,0]
eated = graph[0][0][0]
graph[0][0] = [0,0,int(1e9),graph[0][0][-1]]

for g in graph:
    print(g)
print()
flag = False
while 1:
    # 물고기 이동
    fish = []
    for gr in graph:
        for g in gr:
            fish.append(g)
    fish = sorted(fish,key = lambda x : x[2])
    print(fish)
    q = deque(fish)
    while q:
        n_x, n_y, n_num, n_direc = q.popleft()
        if n_num == int(1e9):
            continue
        while 1:
            n_x += dx[n_direc]
            n_y += dy[n_direc]
            if n_x<0 or n_y<0 or n_x>=4 or n_y>=4:
                n_x -= dx[n_direc]
                n_y -= dy[n_direc]
                n_direc = (n_direc + 1) % 8
                continue
            if graph[n_x][n_y][2] == int(1e9):
                n_x -= dx[n_direc]
                n_y -= dy[n_direc]
                n_direc = (n_direc + 1) % 8
                continue
            temp = graph[n_x-dx[n_direc]][n_y-dy[n_direc]]
            graph[n_x-dx[n_direc]][n_y-dy[n_direc]] = graph[n_x][n_y]
            graph[n_x][n_y] = temp
            break
    # 상어 이동
    sx,sy = shark
    sx, sy, s_name, s_direc = graph[sx][sy]
    while 1:
        sx += dx[s_direc]
        sy += dy[s_direc]
        if sx<0 or sy<0 or sx>=4 or sy>=4:
            flag = True
            break
        if graph[sx][sy] != [-1,-1,-1,-1]:
            eated += graph[sx][sy][2]
            graph[sx][sy] = [graph[sx][sy][0], graph[sx][sy][1], int(1e9),graph[sx][sy][3]]
            graph[sx-dx[s_direc]][sy-dy[s_direc]] = [-1,-1,-1,-1]
            break
    if flag:
        break
    for g in graph:
        print(g)
    print()
    break

print(eated)



