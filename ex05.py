import sys

R,C,T = map(int,sys.stdin.readline().split())
dx = [0,1,-1,0]
dy = [1,0,0,-1]
graph = []
cleaner = []
for i in range(R):
    g = list(map(int,sys.stdin.readline().split()))
    for j in range(C):
        if g[j] == -1:
            cleaner.append([i,j])
    graph.append(g)

for t in range(T):
    new_g = [[0]*C for _ in range(R)]
    for c in cleaner:
        new_g[c[0]][c[1]] = -1
    # 먼지 확산
    for i in range(R):
        for j in range(C):
            if graph[i][j] not in [-1,0]:
                if graph[i][j] >= 5:
                    dust_5 = graph[i][j]//5
                    cnt = 0
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if nx>=0 and ny>=0 and nx<R and ny<C and new_g[nx][ny] != -1:
                            new_g[nx][ny] += dust_5
                            cnt += 1
                    new_g[i][j] += graph[i][j] - (dust_5*cnt)
                else:
                    new_g[i][j] += graph[i][j]
            # if graph[i][j] <5:
            #     new_g[i][j] = graph[i][j]
    # 공기 청정기 실행
    # 위에 공기청정기
    x1,y1 = cleaner[0]
    for r1 in [2,0,1,3]:
        while 1:
            x1 += dx[r1]
            y1 += dy[r1]
            if x1<0 or y1<0 or x1>cleaner[0][0] or y1>=C :
                x1 -= dx[r1]
                y1 -= dy[r1]
                break
            if [x1,y1] == cleaner[0]:
                break
            if new_g[x1][y1]!=0 and new_g[x1-dx[r1]][y1-dy[r1]] == 0:
                temp = new_g[x1][y1]
                new_g[x1][y1] = 0
                new_g[x1-dx[r1]][y1-dy[r1]] = temp
            if new_g[x1][y1]!=0 and new_g[x1-dx[r1]][y1-dy[r1]] == -1:
                new_g[x1][y1] = 0
    # 아래 공기 청정기
    x2,y2 = cleaner[1]
    for r2 in [1,0,2,3]:
        while 1:
            # print(x2,y2)
            x2 += dx[r2]
            y2 += dy[r2]
            if x2<cleaner[1][0] or y2<0 or x2>=R or y2>=C:
                x2 -= dx[r2]
                y2 -= dy[r2]
                break
            if [x2,y2] == cleaner[1]:
                break
            if new_g[x2][y2] != 0 and new_g[x2-dx[r2]][y2-dy[r2]] == 0:
                temp = new_g[x2][y2]
                new_g[x2][y2] = 0
                new_g[x2-dx[r2]][y2-dy[r2]] = temp
            if new_g[x2][y2] != 0 and new_g[x2-dx[r2]][y2-dy[r2]] == -1:
                new_g[x2][y2] = 0

    # 그래프 최신화
    if t != T-1:
        for i in range(R):
            for j in range(C):
                graph[i][j] = new_g[i][j]

result = 0
for n in new_g:
    result += sum(n)
print(result+2)
