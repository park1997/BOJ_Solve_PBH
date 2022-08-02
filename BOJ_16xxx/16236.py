# 아기상어
from collections import deque
import sys
def bfs(x,y,s_s):
    global start, graph, baby_shark_size, eat_list, distance, visited
    q = deque()
    q.append([x,y,s_s])
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    graph[x][y] = 0
    while q:
        a,b,s = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<N and visited[nx][ny] == 0:
                if graph[nx][ny] == 0 or graph[nx][ny] <= s:
                    q.append([nx,ny,s])
                    visited[nx][ny] =  visited[a][b] + 1
                if graph[nx][ny] != 0 and graph[nx][ny] < s:
                    visited[nx][ny] =  visited[a][b] + 1
                    eat_list.append([nx,ny,visited[nx][ny]])
N = int(sys.stdin.readline())
baby_shark_size = 2
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
start = [0,0]
for x in range(N):
    for y in range(N):
        if graph[x][y] == 9:
            start[0] = x
            start[1] = y
            break
result = 0
eat_num = 0
while 1:
    visited = [[0]*N for _ in range(N)]
    eat_list = []
    distance = 0
    bfs(start[0],start[1],baby_shark_size)
    if len(eat_list)!=0:
        eat_list = list(sorted(eat_list,key= lambda x: (x[2],x[0],x[1])))
        start = eat_list[0]
    else:
        break
    eat_num += 1
    result += visited[start[0]][start[1]]
    graph[start[0]][start[1]] = 9
    if eat_num == baby_shark_size:
        baby_shark_size += 1
        eat_num = 0
print(result)