from collections import deque
def bfs(x,y):
    global graph
    visited = [[-1]*(w+2) for _ in range(h+2)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    q = deque()
    q.append([x,y])
    visited[x][y] = 0
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<h+2 and ny<w+2 and visited[nx][ny] == -1:
                if graph[nx][ny]=="." or graph[nx][ny] == "$":
                    visited[nx][ny] = visited[a][b]
                    q.appendleft([nx,ny])
                elif graph[nx][ny] == "#":
                    visited[nx][ny] = visited[a][b] + 1
                    q.append([nx,ny])
    return visited

N = int(input())
for _ in range(N):
    h,w = map(int,input().split())
    graph = []
    graph.append(list("."*(w+2)))
    for i in range(h):
        graph.append(list(map(str,"."+input()+".")))
    graph.append(list("."*(w+2)))
    robber = []
    for i in range(h+2):
        for j in range(w+2):
            if graph[i][j] =="$":
                robber.append([i,j])
    v1 = bfs(robber[0][0],robber[0][1])
    v2 = bfs(robber[1][0],robber[1][1])
    v3 = bfs(0,0)
    result = int(1e9)
    for i in range(h+2):
        for j in range(w+2):
            if v1[i][j] != -1 and v2[i][j]!= -1 and v3[i][j]!=-1: # 이 조건이 없으면 60% 에서 틀렸다고 나옴
                temp = v1[i][j] + v2[i][j] + v3[i][j]

                if graph[i][j] == "*":
                    continue
                if graph[i][j] =="#":
                    temp -= 2
                result = min(result,temp)
    print(result)
