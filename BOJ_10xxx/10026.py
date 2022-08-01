# 적록 색약
import sys
from collections import deque

def bfs(x,y,num,color):
    global tg
    q = deque()
    q.append([x,y])
    tg[x][y] = num
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<N:
                if tg[nx][ny] == color:
                    tg[nx][ny] = num
                    q.append([nx,ny])

N = int(sys.stdin.readline())
num = 0
graph = [list(map(str,sys.stdin.readline())) for _ in range(N)]
tg = [i[:] for i in graph]

for x in range(N):
    for y in range(N):
        if tg[x][y] in ["R","G","B"]:
            bfs(x,y,num,tg[x][y])
            num += 1

tg = [i[:] for i in graph]
for x in range(N):
    for y in range(N):
        if tg[x][y]=="G":
            tg[x][y]="R"

num2 = 0
for x in range(N):
    for y in range(N):
        if tg[x][y] in ["R","B"]:
            bfs(x,y,num2,tg[x][y])
            num2 += 1

print(num,num2)


