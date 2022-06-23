import sys
def destroy(d,s,graph):
    global center
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    a,b = center
    for _ in range(s):
        a += dx[d]
        b += dy[d]
        graph[a][b] = 0
    return graph

def flatten(graph):
    global center, N
    fg = [0] * (N ** 2)
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    a,b = center
    go = 1
    direc = 0
    index = 1
    cnt = 0
    while True:
        cnt += 1
        for i in range(go):
            nx = a + dx[direc]
            ny = b + dy[direc]
            a, b = nx, ny
            if index == N**2 - 1:
                break    
            fg[index] = graph[nx][ny]
            index += 1
        if index == N**2 - 1:
            break
        if cnt % 2 == 0:
            go += 1
        direc = (direc + 1) % 4
    return fg

def make_graph(fg, graph):
    global center, N
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    a, b = center
    go = 1
    direc = 0
    index = 1
    cnt = 0
    while True:
        cnt += 1
        for i in range(go):
            nx = a + dx[direc]
            ny = b + dy[direc]
            a,b = nx, ny
            graph[nx][ny] = fg[index]
            if index == N**2 -1:
                break
            index += 1
        if index == N**2 -1:
            break
        if cnt % 2 == 0:
            go += 1
        direc = (direc + 1) % 4
    return graph

def change_bead(fg):
    temp_bead = [0]
    bead_dic = {1:1,2:1,3:1}
    target = 0
    cnt = 1
    for idx,f in enumerate(fg):
        if idx == 0:
            continue
        if f == target:
            cnt += 1
        else:
            if target != 0:
                temp_bead.append(cnt)
                temp_bead.append(target)
            target = f
            cnt = 1
    return temp_bead + [0] * (N**2 - len(temp_bead))


N,M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
center = [N//2, N//2]
result = 0
for _ in range(M):
    d, s = map(int,sys.stdin.readline().split())
    graph = destroy(d-1,s,graph)
    flat_graph = flatten(graph)
    fg = []
    for idx,f in enumerate(flat_graph):
        if idx == 0:
            fg.append(0)
        if f != 0:
            fg.append(f)
    fg = fg + [0] * (len(flat_graph) - len(fg))

    while True:
        flag = False
        target = 0
        cnt = 0
        for idx,f in enumerate(fg):
            if f == target:
                cnt += 1
            else:
                if cnt >= 4 and target != 0:
                    flag = True
                    result += target * cnt
                    for i in range(idx - cnt, idx,1):
                        fg[i] = 0
                target = f
                cnt = 1
        if not flag:
            break
        temp_fg = []
        for idx,f in enumerate(fg):
            if idx == 0:
                temp_fg.append(0)
            if f != 0:
                temp_fg.append(f)
        fg = temp_fg + [0] * (len(fg) - len(temp_fg))
    
    fg = change_bead(fg)
    graph = make_graph(fg, graph)


print(result)





# new_graph = flatten(graph)

# print(new_graph)