# 백조의 호수
import sys
from collections import deque
def findice(ices):
    global dx,dy,ivisited,ice
    q = deque(ices)
    temp_ice =[]
    while q:
        a,b = q.popleft()
        ivisited[a][b] = True
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<R and 0<=ny<C:
                if graph[nx][ny] == "X" and not ivisited[nx][ny]:
                    temp_ice.append([nx,ny])
                    ivisited[nx][ny] = True 
                    graph[nx][ny] = "."
    ice = temp_ice

def findL(Ls):
    global dx,dy,Lvisited,L
    q = deque(Ls)
    temp_Ls = []
    while q:
        a,b = q.popleft()
        Lvisited[a][b] = True
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<R and 0<=ny<C and not Lvisited[nx][ny]:
                if graph[nx][ny] == ".":
                    Lvisited[nx][ny] = True
                    q.append([nx,ny])
                elif graph[nx][ny] == "X":
                    temp_Ls.append([nx,ny])
                    Lvisited[nx][ny] = True
                if graph[nx][ny] == "L":
                    return True
    L = temp_Ls
    return False

R,C = map(int,sys.stdin.readline().split())
Lvisited = [[False]*C for _ in range(R)]
ivisited = [[False]*C for _ in range(R)]
graph = []
L = []
ice = []
for i in range(R):
    a = list(sys.stdin.readline().strip())
    for j in range(len(a)):
        if "L" == a[j]:
            L.append([i,j])
            ivisited[i][j] = True
            ice.append([i,j])
        if "." == a[j]:
            ice.append([i,j])
    graph.append(a)
del L[1]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

cnt = 0
while 1:
    # print("그래프")
    # for i in graph:
    #     print(i)
    # print("물 위치",ice)
    # print("얼음 방문")
    # for i in ivisited:
    #     print(i)
    # print("백조위치",L)
    # print("백조 방문")
    # for i in Lvisited:
    #     print(i)
    # print()
    if findL(L):
        print(cnt)
        break
    else:
        findice(ice)
        cnt += 1

