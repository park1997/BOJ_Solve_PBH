import sys
from collections import deque
from itertools import combinations

def bfs(graph, visited, act_virus, not_virus):
    q = deque()
    max_time = 0
    for v in act_virus:
        q.append(v)
        visited[v[0]][v[1]] = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        for _ in range(len(q)):
            a,b = q.popleft()
            if [a, b] in not_virus:
                continue
            else:
                for i in range(4):
                    nx = a + dx[i]
                    ny = b + dy[i]
                    if 0<=nx<n and 0<=ny<n:
                        if visited[nx][ny] == -1:
                            if graph[nx][ny] != 1:
                                q.append([nx,ny])
                                visited[nx][ny] = visited[a][b] + 1
                                if [nx, ny] not in not_virus:
                                    max_time = max(max_time, visited[nx][ny])
    for v in visited:
        print(v)
    print()
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1 and graph[i][j] == 0:
                return 100000000

    return max_time

n,m = map(int, sys.stdin.readline().rstrip().split())

virus = []
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if graph[i][j] == 2:
            virus.append([i,j])

act_virus_group = combinations(virus, m)
result_list = []
for act_virus in act_virus_group:
    visited = [[-1] * n for _ in range(n)]
    not_virus = [v for v in virus if v not in act_virus ]
    temp = bfs(graph, visited, act_virus, not_virus)
    result_list.append(temp)

if min(result_list) == 100000000:
    print(-1)
else:
    print(min(result_list))