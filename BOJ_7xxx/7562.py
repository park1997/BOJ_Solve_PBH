# 나이트의 이동
from collections import deque
import sys
def bfs(now,go):
    global visited
    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [1,2,2,1,-1,-2,-2,-1]
    q = deque()
    q.append(now)
    while q:
        a,b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<I and ny<I and visited[nx][ny] == 0:
                q.append([nx,ny])
                visited[nx][ny] = visited[a][b] + 1
                if [nx,ny] == go:
                    return visited[nx][ny]
    pass
N = int(sys.stdin.readline())
for i in range(N):
    I = int(sys.stdin.readline())
    now = list(map(int,sys.stdin.readline().split()))
    go = list(map(int,sys.stdin.readline().split()))
    visited = [[0]*I for _ in range(I)]
    if go==now:
        print(0)
    else:
        print(bfs(now,go))
