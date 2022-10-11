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
def findMaxrix(xs, ys, xd, yd):
    global graph
    matrix = []
    for i in range(xs, xs + xd, 1):
        temp = []
        for j in range(ys, ys + yd, 1):
            temp.append(graph[i][j])
        matrix.append(temp)
    return matrix
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    case = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] != 0:
                end_x, end_y = bfs(i,j)
                print(i,j, end_x, end_y)
                row = abs(end_x - i)
                col = abs(end_y - j)
                case.append([i, j, row + 1, col + 1])
    print(case)
    c = list(permutations(case, len(case)))
    print(c)
    for c in list(permutations(case, len(case))):
        flag = True
        for d in range(len(case) - 1):
            if c[d][3] != c[d + 1][2]:
                flag = False
                break
        if flag:
            print(c)
            for d in range(len(case) - 1):
                xs1, ys1, xd1, yd1 = c[d]
                xs2, ys2, xd2, yd2 = c[d + 1]
                mat1 = findMaxrix(xs1, ys1, xd1, yd1)
                mat2 = findMaxrix(xs2, ys2, xd2, yd2)
            



