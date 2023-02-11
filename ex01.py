import sys
import heapq
def Djikstra():
    q = []
    count = 0
    heapq.heappush(q,[count, start[0], start[1]])
    visited[start[0]][start[1]] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0 , 0]
    while q:
        for _ in range(len(q)):
            cnt, a, b = heapq.heappop(q)
            if [a,b] == end:
                return count - 1
            for i in range(4):
                nx , ny = a, b
                while 1:
                    nx += dx[i]
                    ny += dy[i]
                    if not(0 <= nx < n and 0 <= ny < m):
                        break
                    if graph[nx][ny] == '*':
                        break
                    if visited[nx][ny] > cnt:
                        visited[nx][ny] = cnt
                        heapq.heappush(q, [count, nx, ny])
        count += 1
m, n = map(int, sys.stdin.readline().split())
graph = []
visited = [[int(1e9)] * m for _ in range(n)]
point = []
for i in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))
    for j in range(m):
        if graph[i][j] == 'C':
            point.append([i,j])
start, end = point
result = Djikstra()
print(result)