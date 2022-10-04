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
            if 0 <= nx < 100 and 0 <= ny < 100 and graph[nx][ny] in [0, 3]:
                if graph[nx][ny] == 3:
                    return 1
                q.append([nx, ny])
                graph[nx][ny] = 1
    return 0

T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    graph = [list(map(int, input())) for _ in range(100)]
    graph[1][1] = 1
    r = miro()
    print("#{} {}".format(tc, r))
