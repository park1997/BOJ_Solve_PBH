from collections import deque
import sys
def mapping_num(graph):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited = [[False]*N for _ in range(N)]
    new_graph = [[0]*N for _ in range(N)]
    cnt = 0
    mapping_dic ={}
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt += 1
                q = deque()
                q.append([i,j])
                visited[i][j] = True
                target = graph[i][j]
                new_graph[i][j] = cnt
                group_cnt = 1
                while q:
                    a,b = q.popleft()
                    for d in range(4):
                        nx = a + dx[d]
                        ny = b + dy[d]
                        if nx>=0 and ny>=0 and nx<N and ny<N and not visited[nx][ny]:
                            if target == graph[nx][ny]:
                                q.append([nx,ny])
                                new_graph[nx][ny] = cnt
                                visited[nx][ny] = True
                                group_cnt += 1
                mapping_dic[cnt] = [target,group_cnt]
    # for g in new_graph:
    #     print(g)
    # print(mapping_dic)
    return new_graph, mapping_dic

def find_num(graph):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    close_group = {}
    for i in range(N):
        for j in range(N):
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if nx>=0 and ny>=0 and nx<N and ny<N:
                    if graph[i][j] != graph[nx][ny]:
                        target = str(graph[i][j])+" "+str(graph[nx][ny])
                        if target not in close_group:
                            close_group[target] = 1
                        else:
                            close_group[target] += 1
    # print(close_group)
    return close_group

def cal_score(graph,close_group,mapping_dic):
    r = 0
    for cg in close_group:
        g1,g2 = cg.split()
        g1 = int(g1)
        g2 = int(g2)
        g1_cnt = mapping_dic[g1][1]
        g2_cnt = mapping_dic[g2][1]
        g1_num= mapping_dic[g1][0]
        g2_num = mapping_dic[g2][0]
        close_num = close_group[str(g1) +" " + str(g2)]
        # print(g1_cnt,g2_cnt,g1_num,g2_num)
        r += ((g1_cnt + g2_cnt) * g1_num * g2_num * close_num)
    r = r//2
    return r

def change_graph(graph):
    new_graph = [[0]*N for _ in range(N)]
    mid = N // 2
    row = []
    col = []
    
    for j in range(N):
        row.append(graph[mid][j])
    for i in range(N):
        col.append(graph[i][mid])

    for j2 in range(N):
        new_graph[mid][j2] = col[j2]
    for i2 in range(N-1,-1,-1):
        new_graph[i2][mid] = row[N-i2-1]
    
    # for g in new_graph:
    #     print(g)
    # print()

    g1 = [[0]*mid for _ in range(mid)]
    g2 = [[0]*mid for _ in range(mid)]
    g3 = [[0]*mid for _ in range(mid)]
    g4 = [[0]*mid for _ in range(mid)]

    for i in range(mid):
        for j in range(mid):
            g1[j][mid-i-1] = graph[i][j]
    for i in range(mid):
        for j in range(mid+1,N):
            new_j = j - mid -1
            g2[new_j][mid-i-1] = graph[i][j]
    for i in range(mid+1,N):
        for j in range(mid):
            new_i = i-mid-1
            g3[j][mid-new_i-1] = graph[i][j]
    for i in range(mid+1,N):
        for j in range(mid+1,N):
            new_i = i - mid -1
            new_j = j - mid -1
            g4[new_j][mid-new_i-1] = graph[i][j]
    
    for i in range(N):
        for j in range(N):
            if i == mid or j == mid:
                continue
            if i<mid and j<mid:
                new_graph[i][j] = g1[i][j]
            elif i<mid and j>mid:
                new_graph[i][j] = g2[i][j-mid-1]
            elif i>mid and j<mid:
                new_graph[i][j] = g3[i-mid-1][j]
            elif i>mid and j>mid:
                new_graph[i][j] = g4[i-mid-1][j-mid-1]
    
    # for g in new_graph:
    #     print(g)


    return new_graph


N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
# temp_graph = [g[:] for g in graph]
result = 0
for c in range(4):
    temp_graph = [g[:] for g in graph]
    graph,mapping_dic = mapping_num(graph)
    close_group = find_num(graph)
    score = cal_score(graph,close_group,mapping_dic)
    result += score
    # print(score)
    new_graph = change_graph(temp_graph)
    graph = [g[:] for g in new_graph]
    # print(result)
    # print("*"*10)
    # print()
print(result)