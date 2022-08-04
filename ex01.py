import sys
from collections import deque

def findPrincess():
    global graph, N, M, T
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque([[0,0,0]])
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    ans = int(1e9)
    while q:
        a,b,dis = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<M and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append([nx, ny, dis + 1])
                    if [nx,ny] == [N-1, M-1] and dis + 1 <= T:
                        return dis + 1, ans
                elif graph[nx][ny] == 2:
                    visited[nx][ny] = True
                    distance = dis + abs(nx - (N - 1)) + abs(ny - (M - 1)) + 1
                    if distance <= T:
                        ans = min(distance, ans)
                        
    return "Fail", ans

N, M, T = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

result1, result2 = findPrincess()
if result1 == "Fail" and result2 == int(1e9):
    print("Fail")
elif result1 == "Fail" and result2 != int(1e9):
    print(result2)
else:
    print(min(result1, result2))


