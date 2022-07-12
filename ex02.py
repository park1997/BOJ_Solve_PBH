import sys
from collections import deque

def fishMove(graph):
    global dx, dy, smell_visited, sx, sy
    new_graph = [[deque() for i in range(4)] for _ in range(4)]

    # 물고기 이동
    for i in range(4):
        for j in range(4):
            if len(graph[i][j]) != 0:
                while graph[i][j]:
                    direc = graph[i][j].popleft()
                    first_direc = direc
                    d_cnt = 0
                    nx , ny = None, None
                    while True:
                        d_cnt += 1
                        nx = i + dx[direc]
                        ny = j + dy[direc]
                        if nx>=0 and ny>=0 and nx<4 and ny<4 and [nx,ny] != [sx, sy] and smell_visited[nx][ny] == 0:
                            new_graph[nx][ny].append(direc)
                            break
                        if d_cnt == 8:
                            new_graph[i][j].append(first_direc)
                            break
                        direc = (direc - 1) % 8
                    print([i,j],"->",[nx,ny],direc)
    return new_graph

def sharkMove(sx,sy,graph):
    shark_eat = []
    for d1 in range(4):
        for d2 in range(4):
            for d3 in range(4):
                fm = []
                eat_cnt = 0
                eat_list = []
                nx, ny = sx, sy
                nx += sdx[d1]
                ny += sdy[d1]
                if nx<0 or ny<0 or nx>=4 or ny>=4:
                    eat_cnt = 0
                    continue
                if [nx,ny] not in eat_list and len(graph[nx][ny]) != 0:
                    eat_cnt += len(graph[nx][ny])
                    if [nx,ny] not in fm:
                        fm.append([nx,ny])
                eat_list.append([nx,ny])


                nx += sdx[d2]
                ny += sdy[d2]
                if nx<0 or ny<0 or nx>=4 or ny>=4:
                    eat_cnt = 0
                    continue
                if [nx,ny] not in eat_list and len(graph[nx][ny]) != 0:
                    eat_cnt += len(graph[nx][ny])
                    if [nx,ny] not in fm:
                        fm.append([nx,ny])
                eat_list.append([nx,ny])

                nx += sdx[d3]
                ny += sdy[d3]
                if nx<0 or ny<0 or nx>=4 or ny>=4:
                    eat_cnt = 0
                    continue
                if [nx,ny] not in eat_list and len(graph[nx][ny]) != 0:
                    eat_cnt += len(graph[nx][ny])
                    if [nx,ny] not in fm:
                        fm.append([nx,ny])
                eat_list.append([nx,ny])

                shark_eat.append([eat_cnt,d1,d2,d3,nx,ny,fm])

                eat_cnt = 0
    shark_eat = list(sorted(shark_eat, key = lambda x : (-x[0],x[1],x[2],x[3])))

    print("상어가 먹을거 eat_cnt,d1,d2,d3,nx,ny,fm",shark_eat[0])

    fish_cnt, direc1, direc2, direc3, next_sx, next_sy, fm = shark_eat[0]
    nsx, nsy = sx, sy
    nsx += sdx[direc1]
    nsy += sdy[direc1]
    graph[nsx][nsy] = deque()
    nsx += sdx[direc2]
    nsy += sdy[direc2]
    graph[nsx][nsy] = deque()
    nsx += sdx[direc3]
    nsy += sdy[direc3]
    graph[nsx][nsy] = deque()

    for eat_x, eat_y in fm:
        smell_visited[eat_x][eat_y] = 3


    return next_sx, next_sy

def fishDuplicate(first_state):
    global graph
    for x, y, direction in first_state:
        graph[x][y].append(direction)
    


dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

sdx = [-1,0,1,0]
sdy = [0,-1,0,1]

M, S = map(int,sys.stdin.readline().split())
graph = [[deque() for i in range(4)] for _ in range(4)]


for _ in range(M):
    fx, fy, d = map(int,sys.stdin.readline().split())
    graph[fx-1][fy-1].append(d-1)
    

sx, sy = map(int,sys.stdin.readline().split())
sx -= 1
sy -= 1


fish_smell = []
smell_visited = [[0]*len(graph[0]) for _ in range(len(graph))]

for c in range(S):
    first_state = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if len(graph[i][j]) != 0:
                for ele in graph[i][j]:
                    first_state.append([i,j,ele])
            if smell_visited[i][j] > 0:
                smell_visited[i][j] -= 1
    print("visited")
    for sv in smell_visited:
        print(sv)
    print()

    print("11111")
    for g in graph:
        print(g)
    print()

    print("fish smell",fish_smell)
    
    graph = fishMove(graph)
    print("222222")
    for g in graph:
        print(g)
    print()

    sx, sy = sharkMove(sx,sy,graph)
    print("fish smell",fish_smell)

    print("3333333")
    for g in graph:
        print(g)
    print()
    
    print("sx sy",sx,sy)

    for x, y, direction in first_state:
        graph[x][y].append(direction)

    print(44444444)
    for g in graph:
        print(g)
    print()

    
    

result = 0
for gra in graph:
    for g in gra:
        result += len(g)
print(result)
