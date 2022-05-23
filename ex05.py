import sys
from collections import deque
def waterMove(graph,water):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque()
    for w in water:
        q.append(w)
    temp_water = []
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<R and ny<C:
                if graph[nx][ny] == ".":
                    temp_water.append([nx,ny])
                    graph[nx][ny] = "*"
    return temp_water,graph

def goGosem(graph,start):
    global visited, R, C
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque()
    for st in start:
        visited[st[0]][st[1]] = True
        q.append(st)
    gosem = []
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<R and ny<C and not visited[nx][ny]:
                if graph[nx][ny] == "." or graph[nx][ny] == "D":
                    gosem.append([nx,ny])
                    visited[nx][ny] = True
    return gosem

R,C = map(int,sys.stdin.readline().split())
graph = []
d = []
s = []
w = []
for i in range(R):
    l = list(sys.stdin.readline().strip())
    for j in range(C):
        if l[j] == "D":
            d.append([i,j])
        if l[j] == "S":
            s.append([i,j])
            l[j] = "."
        if l[j] == "*":
            w.append([i,j])
    graph.append(l)
visited = [[False]*C for _ in range(R)]
cnt = 0
flag = False
while True:
    cnt += 1
    temp_s = goGosem(graph,s)
    w, graph = waterMove(graph,w)
    s = []
    for po in temp_s:
        if po not in w:
            s.append(po)
        if po == d[0]:
            flag = True
    if len(s) == 0:
        print("KAKTUS")
        break

    if flag:
        print(cnt)
        break




