import sys
from collections import deque
from itertools import combinations

def simulation(ac, ng):
    global N, M ,D
    dx = [0, -1, 0]
    dy = [-1, 0, 1]
    floor = N
    cnt = 0
    count = -1
    while 1:
        count += 1
        floor -= 1
        target = []
        for a in ac:
            q = deque()
            q.append([a[0] - count, a[1], 1])
            flag = False
            while q:
                a, b, dis = q.popleft()
                for i in range(3):
                    nx = a + dx[i]
                    ny = b + dy[i]
                    if nx >= 0 and ny >= 0 and nx <= floor and ny < M:
                        if ng[nx][ny] == 0 and dis < D:
                            q.append([nx, ny, dis + 1])
                        elif ng[nx][ny] == 1 and dis <= D:
                            if [nx,ny] not in target:
                                target.append([nx, ny])
                            flag = True
                            break
                if flag:
                    break
        
        for t in target:
            x, y = t
            ng[x][y] = 0
            cnt += 1

        if floor == 0:
            break
    return cnt


N, M, D = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
graph.append([-1] * M)

archer = [[N,i] for i in range(M)]
archer_case = list(combinations(archer, 3))

final_result = 0
for ac in archer_case:
    new_graph = [g[:] for g in graph]
    result = simulation(ac, new_graph)
    final_result = max(result, final_result)
print(final_result)
