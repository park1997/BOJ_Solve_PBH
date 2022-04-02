from collections import deque
from itertools import product
grid = ["??b", "abc", "cc?"]
ques = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "?":
            ques.append([i,j])

permu = list(product(["a","b","c"],repeat=len(ques)))
result = 0
for i in range(len(permu)):
    new_grid = [list(g[:]) for g in grid]
    case = permu[i]

    for idx,k in enumerate(ques):
        new_grid[k[0]][k[1]] = case[idx]
    temp = ""
    for ng in new_grid:
        for nng in ng:
            temp += nng
    
    visited = [[0]*len(grid[0]) for _ in range(len(grid))]

    q = deque()
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    check = {"a":False, "b":False,"c":False}
    cnt = 1
    for i1 in range(len(grid)):
        for j1 in range(len(grid[0])):
            if visited[i1][j1] == 0:
                q.append([i1,j1])
                visited[i1][j1] = cnt
                while q:
                    a,b = q.popleft()                    
                    for i in range(4):
                        nx = a + dx[i]
                        ny = b + dy[i]
                        if nx>=0 and ny>=0 and nx<len(grid) and ny<len(grid[0]) and not visited[nx][ny]:
                            if new_grid[a][b] == new_grid[nx][ny]:
                                visited[nx][ny] = cnt
                                q.append([nx,ny])
                cnt += 1
    max_num = -1
    for mg in visited:
        if max_num<max(mg):
            max_num=max(mg)

    if max_num ==len(set(temp)):
        result += 1
    
print(result)

    



