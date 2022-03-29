import sys
from collections import deque
def ball_escape():
    global ball,hole,graph
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque()
    q.append([ball[0][0],ball[0][1],ball[1][0], ball[1][1]])
    # 빨간 구슬이 벽에 사로 막혀 있을떄 
    # flag1 = False
    # for i in range(4):
    #     nx = ball[0][0] + dx[i]
    #     ny = ball[0][1] + dy[i]
    #     if nx>=1 and ny>=1 and nx<N-1 and ny<M-1:
    #         if graph[nx][ny] == ".":
    #             flag1 = True
    #             break
    # if not flag1:
    #     return -1
    visited =[]
    visited.append((ball[0][0],ball[0][1],ball[1][0],ball[1][1]))
    cnt = 0
    while q:
        for _ in range(len(q)):
            rx,ry,bx,by = q.popleft()
            if cnt > 10:
                return -1
            if [rx,ry] == [hole[0],hole[1]]:
                return cnt
            for i in range(4):
                # print(q)
                nrx,nry,nbx,nby=rx,ry,bx,by
                while 1:
                    nrx += dx[i]
                    nry += dy[i]
                    if graph[nrx][nry] == "#":
                        nrx = nrx - dx[i]
                        nry = nry - dy[i]
                        break
                    if graph[nrx][nry] == "O":
                        break
                while 1:
                    nbx += dx[i]
                    nby += dy[i]
                    if graph[nbx][nby] == "#":
                        nbx = nbx - dx[i]
                        nby = nby - dy[i]
                        break
                    if graph[nbx][nby] == "O":
                        break
                
                if graph[nbx][nby] =="O":
                    continue
                # if graph[nrx][nry] == "O":
                #     return cnt + 1

                # 끝까지 밀어넣었는데 구슬 좌표가 같아진 경우
                if [nbx,nby] == [nrx,nry]:
                    # 빨간색이 앞서 있었던 경우
                    if abs(nrx-rx) + abs(nry-ry) < abs(nbx-bx) + abs(nby-by):
                        nbx -= dx[i]
                        nby -= dy[i]
                    else:
                        nrx -= dx[i]
                        nry -= dy[i]
                    # if [rx - dx[i], ry - dy[i]] == [bx,by]:
                    #     nbx = nbx - dx[i]
                    #     nby = nby - dy[i]
                    # # 파란색이 앞서 있었던 경우
                    # elif [bx - dx[i], by - dy[i]] == [rx,ry]:
                    #     nrx = nrx - dx[i]
                    #     nry = nry - dy[i]
                    
                if (nrx,nry,nbx,nby) not in visited:
                    q.append((nrx,nry,nbx,nby))
                    visited.append((nrx,nry,nbx,nby))
        cnt += 1 
    return -1

N,M = map(int,sys.stdin.readline().split())
graph = []
ball = [None,None]
hole = []
for i in range(N):
    g = list(sys.stdin.readline().strip())
    for j in range(M):
        if g[j]=="R":
            ball[0] = (i,j)
        elif g[j] == "B":
            ball[1] = (i,j)
        elif g[j] == "O":
            hole = (i,j)
    graph.append(g)

# for i in graph:
#     print(i)
# print(ball)
# print(hole)

result = ball_escape()
print(result)



