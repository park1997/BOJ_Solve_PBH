import sys
import heapq
from collections import deque

def wall3(start):
    global N, M, K
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append([1, 0, 0, 0, "M"]) # [이동거리, x, y, 벽 부순횟수, 낮 or 밤]
    visited[0][0][0] = 1
    while q:
        dis, x, y, wall_count, time = q.popleft()
        print([dis, x, y, wall_count, time])
        if [x, y] == [N - 1, M - 1]:
            return dis
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0<= ny < M:
                if graph[nx][ny] ==  1 and visited[wall_count + 1][nx][ny] == 0:
                    if time == "M" and wall_count < K:
                        visited[wall_count + 1][nx][ny] = dis + 1
                        q.append([dis + 1, nx, ny, wall_count + 1, "N"])
                    elif time == "N":
                        q.append([dis + 1, x, y, wall_count, "M"])
                        visited[wall_count][x][y] = dis + 1
                elif graph[nx][ny] == 0:
                    if time == "M" and visited[wall_count][nx][ny] == 0:
                        q.append([dis + 1, nx, ny, wall_count, "N"])
                        visited[wall_count][nx][ny] = dis + 1
                    elif time == "N" and visited[wall_count][nx][ny] == 0:
                        q.append([dis + 1, nx, ny, wall_count, "M"])
                        visited[wall_count][nx][ny] = dis + 1
    return -1

N, M, K = map(int, sys.stdin.readline().split())
visited = [[[0] * M for _ in range(N)] for __ in range(K + 1)]
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
result = wall3([0,0])

for i in range(K):
    for v in visited[i]:
        print(v)
    print()
print(result)



