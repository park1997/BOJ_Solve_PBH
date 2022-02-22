import sys
from collections import deque
def bfs(start):
    q = deque([start])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited[start[0]][start[1]] = 0
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            while True:
                if not (nx >=0 and ny>=0 and nx<H and ny<W):
                    break
                if visited[nx][ny] < visited[a][b] + 1:
                    break
                if graph[nx][ny] == "*":
                    break
                q.append([nx,ny])
                visited[nx][ny] = visited[a][b]+1
                nx = nx + dx[i]
                ny = ny + dy[i]


    return
W,H = map(int,sys.stdin.readline().split())
visited = [[int(1e9)]*W for _ in range(H)]
graph = []
c = []
for i in range(H):
    a = list(map(str,sys.stdin.readline().strip()))
    for j in range(W):
        if a[j] == "C":
            c.append([i,j])
    graph.append(a)

bfs(c[0])
print(visited[c[1][0]][c[1][1]]-1)

