import sys
from collections import deque

def bfs(water):
    q = deque(water)
    w = []
    ice = []
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<M:
                if graph[nx][ny] != 0:
                    if [a,b] not in w:
                        w.append([a,b])
                    graph[nx][ny]-=1
                    if graph[nx][ny] == 0 and [nx,ny] not in w:
                        w.append([nx,ny])

    for i in range(N):
        for j in range(M):
            if graph[i][j]!=0:
                ice.append([i,j])
    return w,ice

def check_split(ice):
    visited = [[False]*M for _ in range(N)]
    q = deque()
    q.append(ice[0])
    visited[ice[0][0]][ice[0][1]] = True
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<M:
                if not visited[nx][ny] and graph[nx][ny]!=0:
                    visited[nx][ny] = True
                    q.append([nx,ny])

    for i in ice:
        if not visited[i[0]][i[1]]:
            return True
    return False


N,M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
water = []
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            water.append([i,j])
cnt = 0
while 1:
    cnt += 1
    water,ice = bfs(water)
    if len(ice)!=0:
        if check_split(ice):
            print(cnt)
            break
    else:
        print(0)
        break