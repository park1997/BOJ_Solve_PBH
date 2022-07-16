# 섬의 개수 DFS
from collections import deque
import sys
sys.setrecursionlimit(10**9)
def dfs(x,y):
    global graph
    dx = [0,1,0,-1,1,-1,-1,1]
    dy = [1,0,-1,0,1,-1,1,-1]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and ny>=0 and nx<h and ny<w and graph[nx][ny]==1:
            graph[nx][ny]=0
            dfs(nx,ny)

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
                dfs(x,y)
                cnt += 1
    print(cnt)

    