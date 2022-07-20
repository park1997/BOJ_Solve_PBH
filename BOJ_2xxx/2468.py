# 안전 영역
from collections import deque
def bfs(x,y):
    global graph
    global visited
    q = deque()
    q.append([x,y])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[x][y] = True
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<N and graph[nx][ny]>=h:
                if not visited[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny] = True

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
result = []
for h in range(1,101):
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if graph[x][y]>=h and not visited[x][y]:
                bfs(x,y)
                cnt+=1
    result.append(cnt)
print(max(result))