from collections import deque
def findLand():
    global dx, dy, N, M, visited, q
    while q:
        a,b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                q.append([nx,ny])
                visited[nx][ny] = visited[a][b] + 1
    
    r = 0
    for v in visited:
        r += sum(v)
    return r

dx = [0,0,1,-1]
dy = [1,-1,0,0]
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [[-1] * M for _ in range(N)]
    q = deque()
    for i in range(N):
        g = input()
        for j in range(M):
            if g[j] == "W":
                q.append([i,j])
                visited[i][j] = 0
    result = findLand()
    print("#{} {}".format(test_case, result))