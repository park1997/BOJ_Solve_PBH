# 미로탈출
# n x m 크기의 미로에 갇혔습니다 미로에는 려어 마리의 괴물이 있어 이를 피해 탈출해야합니다
# 현재위치는 (1,1)이며 미로의 출구를 (n,m)위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다
# 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어있습니다.
# 이때 탈출하기위해 움직여야하는 최소 칸의 개수를 구하세요
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
# 답은 10

from collections import deque
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny]==0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]



n,m = map(int,input().split())
graph =[]
for i in range(n):
    graph.append(list(map(int,input())))

# 이동할 네 가지 방향 정의 (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS를 수행한 결과 출력
print(bfs(0,0))