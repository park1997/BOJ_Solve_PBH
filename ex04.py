import sys
import heapq
def mirror(door):
    # 아래 왼쪽 위쪽 오른쪽
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    start, end = door
    q = []
    for d in range(4):
        heapq.heappush(q, [0, d, start[0], start[1]])
        visited[start[0]][start[1]][d] = 0
    while q:
        mirror_cnt, direc, a, b = heapq.heappop(q)
        nx = a + dx[direc]
        ny = b + dy[direc]
        if [nx, ny] == [end[0], end[1]]:
            return mirror_cnt
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == ".":
                if visited[nx][ny][direc] == -1:
                    heapq.heappush(q, [mirror_cnt, direc, nx, ny])
                    visited[nx][ny][direc] = mirror_cnt
                elif visited[nx][ny][direc] > mirror_cnt:
                    heapq.heappush(q, [mirror_cnt, direc, nx, ny])
            # 거울 가능한 자리
            elif graph[nx][ny] == "!":
                # 한번도 방문 안했다면
                if visited[nx][ny][direc] == -1:
                    # 원래 방향 그대로 통과 하는 경우
                    heapq.heappush(q, [mirror_cnt, direc, nx, ny])
                    visited[nx][ny][direc] = mirror_cnt
                    # 왼쪽으로 90도
                    heapq.heappush(q, [mirror_cnt + 1, (direc + 1) % 4, nx, ny])
                    visited[nx][ny][(direc + 1) % 4] = mirror_cnt
                    # 오른쪽으로 90도
                    heapq.heappush(q, [mirror_cnt + 1, (direc + 3) % 4, nx, ny])
                    visited[nx][ny][(direc + 3) % 4] = mirror_cnt
                # 방문한적은 있지만 더 적은 횟수로 방문했다면
                elif visited[nx][ny][direc] >= mirror_cnt:
                    heapq.heappush(q, [mirror_cnt, direc, nx, ny])
                    visited[nx][ny][(direc + 3) % 4] = mirror_cnt + 1

N = int(sys.stdin.readline())
graph = []
door = []
for i in range(N):
    g = list(map(str, sys.stdin.readline().strip()))
    for j in range(N):
        if g[j] == "#":
            door.append([i,j])
    graph.append(g)

visited = [[[-1] * 4 for _ in range(N)] for _ in range(N)]
result = mirror(door)
print(result)