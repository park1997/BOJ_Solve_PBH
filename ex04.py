from collections import deque
import sys
N = int(sys.stdin.readline())
def bfs(start,type):
    global graph, f_visited, w_visited
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    q = deque(start)
    if type == "f":
        for i in start:
            f_visited[i[0]][i[1]] = 1
    elif type == "w":
        for i in start:
            w_visited[i[0]][i[1]] = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<h and ny<w :
                if type == 'f':
                    if graph[nx][ny] != "#" and f_visited[nx][ny] == 0:
                        f_visited[nx][ny] = f_visited[a][b] + 1
                        q.append([nx,ny])
                elif type == "w":
                    if graph[nx][ny] != "#" and w_visited[nx][ny] == 0 and ((f_visited[nx][ny] == 0) or (f_visited[nx][ny] > w_visited[a][b] + 1)):
                        w_visited[nx][ny] = w_visited[a][b] + 1
                        q.append([nx,ny])

for _ in range(N):
    w,h = map(int,sys.stdin.readline().split())
    graph = [list(map(str,sys.stdin.readline().strip())) for _ in range(h)]
    f_visited = [[0]*w for _ in range(h)]
    w_visited = [[0]*w for _ in range(h)]
    s = []
    fire = []
    gate = []
    result = []
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "*":
                fire.append([i,j])
            elif graph[i][j] == "@":
                s.append([i,j])
            if (i==0 or i==h-1 or j ==0 or j==w-1) and (graph[i][j]=="." or graph[i][j]=="@"):
                gate.append([i,j])
    # print(gate)
    bfs(fire,"f")
    bfs(s,"w")
    # for f in f_visited:
    #     print(f)
    # print()
    # for w in w_visited:
    #     print(w)
    for g in gate:
        if w_visited[g[0]][g[1]]!=0:
            result.append(w_visited[g[0]][g[1]])
    if len(result)!=0:
        print(min(result))
    else:
        print('IMPOSSIBLE')


'''
1
7 6
###.###
###.###
#.....#
#.....#
#..@..#
#######
'''