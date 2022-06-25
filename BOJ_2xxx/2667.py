# 단지번호붙히기
from collections import deque

N = int(input())
graph = [list(map(int,input())) for i in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
visited = [[False]*N for _ in range(N)]
q = deque()
result = []
for i in range(N):
    for j in range(N):
        cnt = 1
        # print(i,j)
        if graph[i][j]==1 and not visited[i][j]:
            q.append([i,j])
            visited[i][j] = True
            while q:
                # print(q)
                x,y = q.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx>=0 and ny>=0 and ny<N and nx<N and graph[nx][ny]==1 and not visited[nx][ny]:
                        graph[nx][ny]=0
                        q.append([nx,ny])
                        cnt+=1
            result.append(cnt)
# print()
print(len(result))
result.sort()
for i in result:
    print(i)

