# 유기농 배추
# DFS로 푼 풀이 
import sys
T = int(sys.stdin.readline())
sys.setrecursionlimit(10000)
def dfs(x,y):
    global graph
    global visited
    visited[x][y]=True
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and ny>=0 and nx<N and ny<M:
            if graph[nx][ny]==1 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny)

    

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
                # bfs(x,y)
                dfs(x,y)
                result+=1
    print(result)