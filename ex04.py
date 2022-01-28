from collections import deque
import sys

def bfs(x,y,z):
    global graph, visited,N,M,flag
    q = deque()
    q.append([x,y,z])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited[z][x][y] = 1
    while q and flag:
        a,b,c = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<M:
                if visited[c][nx][ny] == 0 and graph[nx][ny] == 1 and c == 0:
                    q.append([nx,ny,1])
                    visited[1][nx][ny] =  visited[c][a][b] + 1
                elif visited[c][nx][ny] == 0 and graph[nx][ny] == 0:
                    q.append([nx,ny,c])
                    visited[c][nx][ny] =  visited[c][a][b] + 1
            
                if nx == N-1 and ny == M-1:
                    print(visited[c][nx][ny])
                    flag = False
                    break



N,M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for i in range(2)]
flag = True
if N==1 and M ==1 and graph[0][0] == 0:
    flag = False
    print(1)
else:
    bfs(0,0,0)
if flag:
    print(-1)
