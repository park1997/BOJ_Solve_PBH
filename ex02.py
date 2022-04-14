import sys
from collections import deque
def find_group_block():
    global graph
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    block_group = {}
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            t = graph[i][j]
            if t in [0,-1,-2]:
                continue
            q = deque()
            q.append([i,j])
            color_cnt = 1
            # rainbow_cnt = 0
            visited2 = [[False]*N for _ in range(N)]
            visited2[i][j] = True
            visited[i][j] = True
            v2_cnt = 1
            while q:
                a,b = q.popleft()
                for d in range(4):
                    nx = a + dx[d]
                    ny = b + dy[d]
                    if nx>=0 and ny>=0 and nx<N and ny<N and not visited2[nx][ny]:
                        if visited[nx][ny]:
                            continue
                        if graph[nx][ny] == t or graph[nx][ny] == 0:
                            v2_cnt += 1
                            visited2[nx][ny] = True
                            visited[nx][ny] = True
                            q.append([nx,ny])
                            if graph[nx][ny] == t:
                                color_cnt += 1
                            # if graph[nx][ny] == 0:
                            #     rainbow_cnt += 1
            
            # for v in visited2:
            #     print(v)
            # print()
            # for v1 in visited:
            #     print(v1)
            # print()
            temp_block_group =[]
            if color_cnt >= 1 and v2_cnt>=2:
                for v in visited2:
                    print(v)
                print()
                for vi in range(N):
                    for vj in range(N):
                        if visited2[vi][vj]:
                            temp_block_group.append([vi,vj])
                if len(temp_block_group) in block_group:
                    block_group[len(temp_block_group)].append(temp_block_group)
                else:
                    block_group[len(temp_block_group)] = []
                    block_group[len(temp_block_group)].append(temp_block_group)
            for r in range(N):
                for c in range(N):
                    if graph[r][c] == 0:
                        visited[r][c] = False
    return block_group



N,M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
b = find_group_block()
b_keys = list(sorted(b.keys()))
result = 0
while 1:
    b = find_group_block()
    print(b)
    for g in graph:
        print(g)
    print()
    b_keys = list(sorted(b.keys()))
    if len(b_keys) ==0:
        break
    target = b[b_keys[-1]]
    block_idx = 0
    # 크기가 가장 큰 블록이 1개인 경우
    if len(target) == 1:
        for t in target[0]:
            # 그래프 요소 삭제(삭제 된 애는 -2)
            graph[t[0]][t[1]] = -2
        result += len(target[0])**2
    # 크기가 가장 큰 블록이 1개가 아닌경우
    else:
        rainbow_cnt = []
        # 군집 별 무지개 블록수 구하기 
        for idx,tar in enumerate(target):
            temp_rainbow_cnt = 0
            for t in tar:
                if graph[t[0]][t[1]] == 0:
                    temp_rainbow_cnt += 1
            rainbow_cnt.append(temp_rainbow_cnt)
        # 무지개 블록수가 같은게 여러개 인 경우
        if rainbow_cnt.count(max(rainbow_cnt)) != 1:
            # 기준 블록 리스트
            target_block = []
            for tar in target:
                for t in tar:
                    if graph[t[0]][t[1]] != 0:
                        target_block.append(t)
                        break
            result_block = [-1,-1]
            # 행이 큰거 열이 큰거 찾기
            for idx,gi in enumerate(target_block):
                if gi[0] > result_block[0]:
                    result_block[0], result_block[1] = gi[0], gi[1]
                    block_idx = idx
                elif gi[0] == result_block[0]:
                    if gi[1] > result_block[1]:
                        result_block[0], result_block[1] = gi[0], gi[1]
                        block_idx = idx
        # 무지개 블록수가 같은게 한개인 경우
        else:
            block_idx = rainbow_cnt.index(max(rainbow_cnt))
        
        # 그래프 에서 삭제
        for t in target[block_idx]:
            # 그래프 요소 삭제(삭제 된 애는 -2)
            graph[t[0]][t[1]] = -2
        result += len(target[block_idx])**2
    for g in graph:
        print(g)
    print()
    # 중력 작용
    for i in range(N-2,-1,-1):
        for j in range(N):
            if graph[i][j] > -1:
                r =i
                while 1:
                    if 0<=r+1< N and graph[r+1][j] == -2:
                        graph[r+1][j] = graph[r][j]
                        graph[r][j] = -2
                        r += 1
                    else:
                        break
    for g in graph:
        print(g)
    print()
    temp_graph = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp_graph[i][j] = graph[j][N-i-1]

    for i in range(N):
        for j in range(N):
            graph[i][j] = temp_graph[i][j]
    for g in graph:
        print(g)
    print()
    # 중력 작용
    for i in range(N-2,-1,-1):
        for j in range(N):
            if graph[i][j] > -1:
                r =i
                while 1:
                    if 0<=r+1< N and graph[r+1][j] == -2:
                        graph[r+1][j] = graph[r][j]
                        graph[r][j] = -2
                        r += 1
                    else:
                        break
    for g in graph:
        print(g)
    print()

    # print(target)
    # break

print(result)


'''
6 1
0 0 0 0 0 1
-1 -1 0 -1 -1 0
-1 0 2 -1 0 -1
-1 -1 -1 0 0 -1
1 1 -1 -1 0 -1
1 1 -1 0 0 3

80
'''