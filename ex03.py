import sys
from collections import deque

def bfs(x,y):
    global visited
    q = deque()
    q.append([x])
    dx = [2,-1,1]
    visited[x] = 1
    while q:
        a = q.popleft()[0]
        for i in range(3):
            if i==0:
                nx = a * dx[i]
            else:
                nx = a + dx[i]
            if nx>=0 and nx<len(visited) and visited[nx] == 0:
                visited[nx] =  visited[a] + 1
                q.append([nx])

X,Y = map(int,sys.stdin.readline().split())
if X<Y:
    visited = [0]*(max(X,Y)+1)
    bfs(X,Y)
    print(visited[Y]-1)
    # print(visited)
else:
    print(X-Y)