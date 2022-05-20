import sys
def fire_shark(graph):
    global dx,dy
    temp_graph = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) != 0:
                for g in graph[i][j]:
                    m,s,d = g
                    nx = (i + s * dx[d]) % N
                    ny = (j + s * dy[d]) % N
                    temp_graph[nx][ny].append((m,s,d))
    return temp_graph
    
def spread_fire(graph):
    temp_graph = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) >= 2:
                even = 0
                temp_m = 0
                temp_s = 0
                for tg in graph[i][j]:
                    m1,s1,d1 = tg
                    # 방향이 짝수인지
                    if d1 % 2 == 0:
                        even += 1
                    temp_m += m1
                    temp_s += s1
                temp_m = temp_m // 5
                temp_s = temp_s // len(graph[i][j])
                if temp_m != 0:
                    if even == len(graph[i][j]) or even == 0:
                        for d in [0,2,4,6]:
                            temp_graph[i][j].append((temp_m,temp_s,d))
                    else:
                        for d in [1,3,5,7]:
                            temp_graph[i][j].append((temp_m,temp_s,d))
                else:
                    temp_graph[i][j] = []
            elif len(graph[i][j]) == 1:
                temp_graph[i][j].append(graph[i][j][0])
    return temp_graph



N,M,K = map(int,sys.stdin.readline().split())
fire = []
graph = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r,c,m,s,d = map(int,sys.stdin.readline().split())
    fire.append([r-1,c-1,m,s,d])
    graph[r-1][c-1].append((m,s,d))
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(K):
    graph = fire_shark(graph)
    graph = spread_fire(graph)

result = 0
for gra in graph:
    for gr in gra:
        for g in gr:
            result += g[0]
print(result)

