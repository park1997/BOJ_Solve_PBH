from collections import deque
import sys
def bfs(x,y,s_s):
    global graph, baby_shark_size, eat_list, visited
    q = deque() # Queue 선언
    q.append([x,y,s_s]) # 시작 위치 x,y와 아기상어의 크기 append
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    graph[x][y] = 0 # 아기상어의 처음 위치를 0으로 비워준다.
    while q:
        a,b,s = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<N and visited[nx][ny] == 0:
                if graph[nx][ny] == 0 or graph[nx][ny] <= s: # 아기상어가 갈 수 있는 빈칸(0) 이거나 아기상어의 크기보다 작거나 같은 크기를 가진 물고기 인 경우 => 이동은 할 수 있음
                    q.append([nx,ny,s]) # 이동 할 수 있는 다음위치를 Queue에 저장
                    visited[nx][ny] =  visited[a][b] + 1  # 이전에 왔던 곳 + 1 을 하여 그곳까지 갈 수 있는 거리를 저장한다.
                if graph[nx][ny] != 0 and graph[nx][ny] < s: # 이동하려고 간 위치가 아닌 아기상어가 먹을 수 있는 물고기의 위치를 찾는다
                    visited[nx][ny] =  visited[a][b] + 1 # 그곳까지 도달하기 위한 거리를 저장한다
                    eat_list.append([nx,ny,visited[nx][ny]]) # 먹을 수 있는 물고기의 위치를 저장한다.
N = int(sys.stdin.readline()) # 공간의 크기 N 입력
baby_shark_size = 2 # 아기상어의 처음 Size
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)] # 아기 상어와 다른 물고기가 있는 그래프 
start = [0,0] # 아기 상어가 있는 처음 위치
for x in range(N):
    for y in range(N):
        if graph[x][y] == 9: # 아기 상어의 위치를 찾았을 시 
            start[0] = x    # 아기 상어의 첫 위치 X값을 저장해준다
            start[1] = y    # 아기 상어의 첫 위치 Y값을 저장해준다
            break   # 아기상어는 1명 밖에 없으므로 찾으면 그냥 break 해준다.
result = 0  # 최종 결과가 저장될 변수
eat_num = 0 # 아기상어가 먹은 물고기의 개수가 들어갈 변수
while 1:
    visited = [[0]*N for _ in range(N)] # 아기상어가 먹을 수 있는 물고기의 위치를 찾기위해 bfs를 돌릴 때 방문하기위한 거리가 저장될 2차원 행렬
    eat_list = [] # 아기상어가 먹을 수 있는 물고기의 위치가 저장될 리스트
    bfs(start[0],start[1],baby_shark_size)  # 시작점 x,y와 아기상어의 크기가 매개변수로 들어간 bfs 함수
    if len(eat_list)!=0: # 먹을 물고기를 찾은 경우
        eat_list = list(sorted(eat_list,key= lambda x: (x[2],x[0],x[1])))   # 가장 가까우면서 가장 위쪽에 있으면서 가장 왼쪽에 있는 물고기를 먹기위해 정렬을 수행한다.
        start = eat_list[0] # 선정될 다음에 먹을 고기 의 위치를 start 에 저장한다.
    else:   # bfs를 돌렸을때 아기상어가 더이상 먹을 물고기가 존재 하지 않았을 시 반복문을 빠져 나가고 result 를 출력한다. 
        break
    eat_num += 1 # bfs로 물고기를 찾았으므로 물고기를 먹은 횟수 +1
    result += visited[start[0]][start[1]] # 찾은 먹을 물고기를 먹으러 가는 거리를 result 에 더해준다. 
    graph[start[0]][start[1]] = 9   # 찾은 먹이위치에 상어를 배치 시킨다.
    if eat_num == baby_shark_size: # 아기상어 사이즈의 개수만큼 먹이를 먹었을 경우
        baby_shark_size += 1    # 아기 상어의 크기를 +1 증가시켜 준다.
        eat_num = 0 # 먹은 먹이의 개수 초기화
print(result)