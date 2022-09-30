from collections import deque
def miro():
    q = deque([[1, 1]])
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while q:
        a, b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny] and graph[nx][ny] in ["0","3"]:
                if graph[nx][ny] == "3":
                    return 1
                q.append([nx, ny])
                visited[nx][ny] = True
    return 0

T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    graph = [list(map(str,input())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]
    visited[1][1] = True
    r = miro()
    print("#{} {}".format(tc, r))
