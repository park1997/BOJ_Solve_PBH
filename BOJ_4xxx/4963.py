# 섬이 개수
from collections import deque
import sys
def bfs(x,y):
    global graph
    q = deque()
    q.append([x,y])
    graph[x][y] = 0
    dx = [0,1,0,-1,1,-1,-1,1]
    dy = [1,0,-1,0,1,-1,1,-1]
    while q:
        a,b = q.popleft()
        for k in range(8):
            nx = a+dx[k]
            ny = b+dy[k]
            if nx>=0 and ny>=0 and nx<h and ny<w and graph[nx][ny]==1:
                graph[nx][ny] = 0
                q.append([nx,ny])
while 1:
    w,h = map(int,sys.stdin.readline().split())
    if w==0 and h==0:
        break
    graph = []
    cnt = 0
    for i in range(h):
        graph.append(list(map(int,sys.stdin.readline().split())))
    for x in range(h):
        for y in range(w):
            if graph[x][y]==1:
                bfs(x,y)
                cnt += 1
    print(cnt)

    