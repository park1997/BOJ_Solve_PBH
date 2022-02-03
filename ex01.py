import sys
def go(r,c,d):
    global visited, graph, result
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    cleaner = [r,c] # 청소기의 현재 위치가 저장됨
    graph[r][c] = -1 # 현재 청소기의 위치를 -1 로 대입
    visited[r][c] = True # 현재 청소기의 위치를 방문했다고 처리 
    result += 1
    while 1:
        flag = False
        flag2 = False
        for _ in range(4): # 동서남북방향에서 갈수있는 곳인지 조사해야하므로 4번 for loop를 돌림
            d += 3  # 90도 회전하기위한 Index 처리
            d %= 4  # 90도 회전하기위한 Index 처리
            nx = cleaner[0] + dx[d] # 90도 회전하고 청소기가 이동한 x좌표
            ny = cleaner[1] + dy[d] # 90도 회전하고 청소기가 이동한 y좌표
            if nx>=0 and ny>=0 and nx<N and ny<M:   # 청소기가 graph를 벗어나지 않으면서 
                if graph[nx][ny] == 0 and not visited[nx][ny]: # 청소기가 방문하지 않은 곳 이면서 갈 수있는 곳이라면 
                    result += 1 # 청소기가 이동한 거리 +=1
                    graph[cleaner[0]][cleaner[1]] = 0 # 청소기의 원래위치를 빈곳으로 만듬
                    graph[nx][ny] = -1 # 청소기가 이동한 지역에 청소기를 둠
                    cleaner = [nx,ny]   # 이동한 청소기의 위치로 위치를 초기화 함
                    visited[nx][ny] = True  # 방문 처리 
                    flag2 = True
                    break
        flag = True
        if flag and not flag2:   # 만약 청소기가 동서남북 모두 확인했지만 이미 청소했거나 벽인 경우 
            nx = cleaner[0] + dx[d]*(-1)    # 청소기가 바라보고있는 위치의 반대방향으로 이동한 청소기의 x좌표
            ny = cleaner[1] + dy[d]*(-1)    # 청소기가 바라보고있는 위치의 반대방향으로 이동한 청소기의 y좌표
            if graph[nx][ny] == 0:  # 만약 반대방향으로 이동할 청소기의 위치가 벽이 아닌 빈 곳이라면 
                graph[cleaner[0]][cleaner[1]] = 0   # 청소기가 있던자리를 빈자리로 만들고
                graph[nx][ny] = -1  # 후진한 자리로 청소기를 이동
                cleaner = [nx,ny] # 현재 청소기의 실제위치를 초기화 
            elif graph[nx][ny] == 1:    # 계속 후진을 하다가 벽을 만나게 된다면 
                break # while loop를 빠져 나오게 됨
    return print(result) # 탐색이 종료 되었으므로 result를 출력하면서 return 
N,M = map(int,sys.stdin.readline().split())
r,c,d = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
result = 0
go(r,c,d)

for 