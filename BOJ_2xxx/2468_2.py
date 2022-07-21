# 안전 영역 DFS
import sys
sys.setrecursionlimit(10**9)
def dfs(x,y):
    global visited
    global graph
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and ny>=0 and nx<N and ny<N and graph[nx][ny]>=h:
            if not visited[nx][ny]:
                dfs(nx,ny)


N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
result = []
for h in range(1,101):
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if graph[x][y]>=h and not visited[x][y]:
                dfs(x,y)
                cnt+=1
    result.append(cnt)
print(max(result))