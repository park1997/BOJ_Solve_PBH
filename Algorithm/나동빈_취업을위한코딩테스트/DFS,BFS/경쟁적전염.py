import sys
N,K = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
temp_g = []
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(graph[i][j])
    temp_g.append(temp)

S,X,Y = map(int,sys.stdin.readline().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(S):
    for f in range(1,K+1):
        for i in range(N):
            for j in range(N):
                if temp_g[i][j] == f:
                    for d in range(4):
                        x = i+dx[d]
                        y = j+dy[d]
                        if x>=0 and y>=0 and x<N and y<N and graph[x][y]==0:
                            graph[x][y] = graph[i][j]
    temp_g = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(graph[i][j])
        temp_g.append(temp)
print(graph[X-1][Y-1])
    
