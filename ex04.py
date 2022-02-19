from collections import deque
import sys

def bfs(s):
    global W,H
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque([s])
    visited[s[0]][s[1]] = 0
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            while 1:
                # 범위를 벗어날 때 
                if nx<0 or ny<0 or nx>=H or ny>=W:
                    break
                # 벽을 만날 때 
                if graph[nx][ny] == "*":
                    break
                # 지난적 있는데 그렇게 가면 너무 많은 거울이 필요해서 break
                # 방문 안한건 INF라 어차피 visited[nx][ny] 가 더 큼
                if visited[nx][ny] < visited[a][b] + 1:
                    break
                q.append([nx,ny])
                visited[nx][ny] = visited[a][b] + 1
                # 같은 방문으로 다음 방문점 방문
                nx += dx[i]
                ny += dy[i]


W,H = map(int,sys.stdin.readline().split())
graph = []
C = []
visited = [[int(1e9)]*W for _ in range(H)]
for i in range(H):
    a = list(sys.stdin.readline().strip())
    for j in range(W):
        if a[j] == "C":
            C.append([i,j])
    graph.append(a)
bfs(C[0])
print(visited[C[1][0]][C[1][1]]-1)

