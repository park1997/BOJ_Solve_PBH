'''
4 6
101111
101010
101011
111011
'''
from collections import deque
N,M = map(int,input().split())
graph = [list(map(int,input())) for i in range(N)]
dx = [0,-1,1,0]
dy = [-1,0,0,1]
q = deque()
q.append([0,0])
while len(q)!=0:
    x,y = q.popleft()
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if a>=0 and b>=0 and a<N and b<M and graph[a][b] == 1:
            q.append([a,b])
            graph[a][b] = graph[x][y] + 1
print(graph[N-1][M-1])
