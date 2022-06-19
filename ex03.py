import sys
from collections import deque
def rotate(l):
    length = 2 ** l
    left_top = []
    x = 0
    y = 0
    while True:
        if 0<=y<NN:
            left_top.append([x,y])
            y += length
        else:
            x += length
            y = 0
        if x>=NN:
            break
    for nx,ny in left_top:
        new_graph = []
        for y in range(ny, ny + length, 1):
            temp = []
            for x in range(nx + length - 1, nx - 1, -1):
                temp.append(graph[x][y])
            new_graph.append(temp)

        for i in range(length):
            for j in range(length):
                graph[nx + i][ny + j] = new_graph[i][j]
    minus_ = []
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    for i in range(NN):
        for j in range(NN):
            if graph[i][j] == 0:
                continue
            ice_cnt = 0
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0<=nx<NN and 0<=ny<NN:
                    if graph[nx][ny] >= 1:
                        ice_cnt += 1
            if ice_cnt >= 3:
                pass
            else:
                minus_.append([i,j])

    for mgx,mgy in minus_:
        graph[mgx][mgy] -= 1


def bfs(graph):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    visited = [[False]*NN for _ in range(NN)]
    q = deque()
    
    max_cnt = 0
    for i in range(NN):
        for j in range(NN):
            if graph[i][j] >= 1:
                m_cnt = 1
                q.append([i,j])
                visited[i][j] = True
                while q:
                    a,b = q.popleft()
                    for i in range(4):
                        nx = a + dx[i]
                        ny = b + dy[i]
                        if nx>=0 and ny>=0 and nx<NN and ny<NN and not visited[nx][ny] and graph[nx][ny] >= 1:
                            visited[nx][ny] = True
                            q.append([nx,ny])
                            m_cnt += 1
                if max_cnt < m_cnt:
                    max_cnt = m_cnt
    return max_cnt


N, Q = map(int, sys.stdin.readline().split())
NN = 2 ** N
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(NN)]
L = list(map(int,sys.stdin.readline().split()))

for l in L:
    rotate(l)


result1 = 0
for g in graph:
    result1 += sum(g)
print(result1)
result2 = bfs(graph)
print(result2)




