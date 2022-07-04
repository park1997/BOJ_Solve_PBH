import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    graph.append(arr)

def dfs(x,y, h):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] <= h:
        temp[x][y] = 1
        return False
    if temp[x][y] == 0:
        temp[x][y] = 1
        dfs(x-1, y, h)
        dfs(x, y-1, h)
        dfs(x+1, y, h)
        dfs(x, y+1, h)
        return True
    return False

result = []
for height in range(max(max(graph))+1):
    temp = [[0] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= height and dfs(i, j, height):
                count += 1
    result.append(count)
print(max(result))