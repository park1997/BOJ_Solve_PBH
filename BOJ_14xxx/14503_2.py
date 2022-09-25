# 로봇청소기
import sys
def go(r,c,d):
    global visited, graph, result
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    cleaner = [r,c]
    graph[r][c] = -1
    visited[r][c] = True
    result += 1
    while 1:
        flag = False
        flag2 = False
        for _ in range(4):
            d += 3
            d %= 4
            nx = cleaner[0] + dx[d]
            ny = cleaner[1] + dy[d]
            if nx>=0 and ny>=0 and nx<N and ny<M:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    result += 1
                    graph[cleaner[0]][cleaner[1]] = 0
                    graph[nx][ny] = -1
                    cleaner = [nx,ny]
                    visited[nx][ny] = True
                    flag2 = True
                    break
        flag = True
        if flag and not flag2:
            nx = cleaner[0] + dx[d]*(-1)
            ny = cleaner[1] + dy[d]*(-1)
            if graph[nx][ny] == 0:
                graph[cleaner[0]][cleaner[1]] = 0
                graph[nx][ny] = -1
                cleaner = [nx,ny]
            elif graph[nx][ny] == 1:
                break
    return print(result)
N,M = map(int,sys.stdin.readline().split())
r,c,d = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
result = 0
go(r,c,d)