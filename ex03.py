import sys
from collections import deque
def bfs(start):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque([start])
    while q:
        a,b,c = q.popleft()
        if [a,b] == [Ex-1,Ey-1]:
            return visited[c][a][b]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<M and not visited[c][nx][ny]:
                if graph[nx][ny] == 0 and c == 0:
                    q.append([nx,ny,0])
                    visited[0][nx][ny] = visited[c][a][b] + 1
                elif graph[nx][ny] == 0 and c == 1:
                    q.append([nx,ny,1])
                    visited[1][nx][ny] = visited[c][a][b] + 1
                elif graph[nx][ny] == 1 and c == 0:
                    q.append([nx,ny,1])
                    visited[1][nx][ny] = visited[c][a][b] + 1
    return -1


N,M = map(int,sys.stdin.readline().split())
Hx,Hy = map(int,sys.stdin.readline().split())
Ex,Ey = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for i in range(2)]
print(bfs([Hx-1,Hy-1,0]))

'''
5 6
1 1
5 6
0 1 1 1 0 0
0 1 1 0 0 0
0 1 0 0 1 0
0 1 0 0 1 0
0 1 0 0 0 0
'''