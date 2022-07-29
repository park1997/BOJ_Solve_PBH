# 영역 구하기
import sys
from collections import deque
def bfs(x,y,r1):
    global graph
    q = deque()
    q.append([x,y])
    graph[x][y] = r1
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<M:
                if graph[nx][ny]==0:
                    q.append([nx,ny])
                    graph[nx][ny] = r1
                    
M,N,K = map(int,input().split())
graph = [[0]*M for i in range(N)]
r1 = 2
result = []
for i in range(K):
    a,b,c,d = map(int,input().split())
    a = a
    b = b
    c = c - 1
    d = d - 1
    for i in range(a,a+abs(c-a)+1):
        for j in range(b,b+abs(b-d)+1):
            graph[i][j] = 1

for x in range(N):
    for y in range(M):
        if graph[x][y] == 0:
            bfs(x,y,r1)
            r1 += 1
for i in range(2,r1):
    cnt = 0
    for g in graph:
        cnt+=g.count(i)
    result.append(cnt)
print(r1-2)
result.sort()
print(*result)