import sys
from collections import deque
def bfs(start):
    global graph,R,C,dx,dy
    q = deque()
    q.append(start)
    visited2 = [[False]*C for _ in range(R)]
    visited2[start[0]][start[1]] = True
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<R and ny<C:
                if graph[nx][ny] == "." and not visited2[nx][ny]:
                    q.append([nx,ny])
                    visited2[nx][ny] = True
                if graph[nx][ny] == "L" and not visited2[nx][ny]:
                    return True
    return False 
R,C = map(int,sys.stdin.readline().split())
graph = []
L = []
for i in range(R):
    a = list(sys.stdin.readline().strip())
    for j in range(len(a)):
        if "L" == a[j]:
            L.append([i,j])
            break
    graph.append(a)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

cnt =0
while 1:
    if bfs(L[0]):
        break
    else:
        cnt += 1
        visited = [[False]*C for _ in range(R)]
        for x in range(R):
            for y in range(C):
                if graph[x][y] == "." and not visited[x][y]:
                    visited[x][y] = True
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx>=0 and ny>=0 and nx<R and ny<C:
                            if graph[nx][ny] == "X":
                                graph[nx][ny] = "."
                                visited[nx][ny] = True
print(cnt)

