import sys 
input = sys.stdin.readline

N, L , R = map(int,input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(x,y) :
    global sum, cnt ,ok 
    sum+=graph[x][y]
    cnt +=1 
    visited[x][y] = 1
    visited2.append([x,y])
    for a in range(4):
        nx = x+dx[a] 
        ny = y+dy[a]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and L<=abs(graph[nx][ny]-graph[x][y])<=R:
            ok = False
            dfs(nx,ny)
    return sum // cnt

graph = []
count = 0

for i in range(N):
    graph.append(list(map(int,input().split())))

while True :
    visited = [[0]*N for _ in range(N)]
    ok = True
    nums = []
    for i in range(N):
        for j in range(N):
            sum = 0
            cnt = 0 
            visited2 = []
            if visited[i][j] == 0:
                avg = dfs(i,j)
                if cnt >= 2 :
                    for xy in visited2 :
                        nums.append([avg,xy])
                    
    if ok :
        break


    for i in nums:
        x,y = i[1]
        graph[x][y] = i[0]
    

    count +=1


print(count)