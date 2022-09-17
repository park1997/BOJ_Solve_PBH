import sys

from ex01 import sharkMove

def findFishNum(graph,num):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == num:
                return i, j

def findShark(graph):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == 0:
                return i, j

def fishMove():
    global graph, pass_fish
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,-1,-1,-1,0,1,1,1]
    for move_fish in range(1,17,1):
        if move_fish == pass_fish:
            continue
        
        x, y = findFishNum(graph, move_fish)
        direc = graph[x][y][1]
        cnt = 0
        while True:
            nx = x + dx[direc]
            ny = y + dy[direc]
            if 0 <= nx < 4 and 0 <= ny < 4 and graph[nx][ny][0] != 0:
                print(move_fish,nx,ny,i)
                temp_a, temp_b = graph[nx][ny]
                graph[nx][ny][0], graph[nx][ny][1] = graph[x][y]
                graph[x][y][0], graph[x][y][1] = temp_a, temp_b
                break
            else:
                cnt += 1
                direc = (direc + 1) % 8
                if cnt == 8:
                    break
        
        for gra in graph:
            # 박병현 메롱 나도 16인치 사구시땅
            print(gra)
        print()

    return graph

def backTracking(x,y):
    
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,-1,-1,-1,0,1,1,1]

    g = fishMove()
    nx, ny = shark_x, shark_y
    shark_direc = graph[shark_x][shark_y]
    while 1:
        nx += dx[shark_direc]
        ny += dy[shark_direc]
        if nx >= 0 and ny >= 0 and nx < 4 and ny < 4:
            backTracking(nx,ny)


    return


graph = []
for i in range(4):
    a1,b1, a2,b2, a3,b3, a4,b4 = map(int,sys.stdin.readline().split())
    graph.append([[a1, b1 - 1],[a2, b2 - 1],[a3, b3 - 1],[a4, b4 - 1]])


pass_fish = graph[0][0][0]
graph[0][0] = [0, graph[0][0][1]]
shark_x, shark_y = 0, 0




for gra in graph:
    print(gra)

backTracking()


