# 유기농 배추
from collections import deque
import sys
T = int(sys.stdin.readline())
def bfs(x,y):
    global graph
    global visited
    q = deque()
    q.append([x,y])
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    while q:
        x1,y1 = q.popleft()
        for i in range(4):
            x2 = x1+dx[i]
            y2 = y1+dy[i]
            if x2>=0 and y2>=0 and x2<N and y2<M:
                if graph[x2][y2]==1 and not visited[x2][y2]:
                    visited[x2][y2] = True
                    q.append([x2,y2])
for i in range(T):
    result = 0
    M,N,K = map(int,sys.stdin.readline().split())
    graph = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    for j in range(K):
        a,b = map(int,sys.stdin.readline().split())
        graph[b][a] = 1
    for x in range(N):
        for y in range(M):
            if graph[x][y]==1 and not visited[x][y]:
                bfs(x,y)
                result+=1
    print(result)
