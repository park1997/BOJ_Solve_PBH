from collections import deque
from itertools import permutations
def bfs(x,y):
    visited[x][y] = True
    q = deque([[x,y]])
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    last = None
    while q:
        a, b = q.popleft()
        for d in range(4):
            nx = a + dx[d]
            ny = b + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] != 0:
                visited[nx][ny] = True
                q.append([nx,ny])
                last = [nx, ny]
    return last
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    case = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] != 0:
                end_x, end_y = bfs(i,j)
                row = abs(end_x - i)
                col = abs(end_y - j)
                case.append([i, j, row + 1, col + 1])
    
    c = list(permutations(case, len(case)))
    result = int(1e9)
    for c in list(permutations(case, len(case))):
        flag = True
        for d in range(len(case) - 1):
            if c[d][3] != c[d + 1][2]:
                flag = False
                break
        if flag:
            temp = 0
            new_xd = c[0][2]
            for d in range(len(case) - 1):
                xs1, ys1, xd1, yd1 = c[d]
                xs2, ys2, xd2, yd2 = c[d + 1]
                temp += new_xd * xd2 * yd2
                new_xd = xd1
            new_xd = c[-1][3]
            temp2 = 0
            for d in range(len(case) - 1, 0, -1):
                xs1, ys1, xd1, yd1 = c[d]
                xs2, ys2, xd2, yd2 = c[d - 1]
                temp2 += xd2 * xd1 * new_xd
                new_xd = yd1
            result = min(result, temp, temp2)
    print("#{} {}".format(test_case, result))