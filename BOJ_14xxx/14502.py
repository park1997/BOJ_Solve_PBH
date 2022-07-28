# 연구소
from collections import deque
from itertools import combinations
import sys
def bfs(tg,x,y,num):
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
            if nx>=0 and ny>=0 and nx<N and ny<M:
                if tg[nx][ny]==0:
                    q.append([nx,ny])
                    tg[nx][ny] = num

N,M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
wall = list(combinations([i for i in range(N*M)],3))
result = -1
for w in wall:
    w1,w2,w3 = w
    w1 = [w1//M,w1%M]
    w2 = [w2//M,w2%M]
    w3 = [w3//M,w3%M]
    if graph[w1[0]][w1[1]]==0 and graph[w2[0]][w2[1]]==0 and graph[w3[0]][w3[1]]==0:
        tg = [i[:] for i in graph]
        tg[w1[0]][w1[1]] = 1
        tg[w2[0]][w2[1]] = 1
        tg[w3[0]][w3[1]] = 1
        for x in range(N):
            for y in range(M):
                if tg[x][y] == 2:
                    bfs(tg,x,y,2)
        cnt = 0
        for x in range(N):
            for y in range(M):
                if tg[x][y] == 0:
                    cnt += 1
        if cnt > result:
            result = cnt
print(result)
