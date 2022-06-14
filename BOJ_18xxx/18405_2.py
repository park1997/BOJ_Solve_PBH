import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())
graph = []
d = []
for i in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
    for j in range(N):
        if graph[i][j]!=0:
            d.append([graph[i][j],i,j])
d.sort()
q = deque(d)

S,X,Y = map(int,sys.stdin.readline().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for s in range(S):
    temp = []
    while q:
        e,x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<N and graph[nx][ny]==0:
                graph[nx][ny]= graph[x][y]
                temp.append([graph[nx][ny],nx,ny])
    for i in temp:
        q.append(i)
print(graph[X-1][Y-1])

