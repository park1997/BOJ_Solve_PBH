from collections import deque
import sys

def bfs() :
    result = 10000000
    que = deque()
    que.append([0,0,0])

    visited[0][0]= True

    while que:
        x,y,count= que.popleft()
        if x== N-1 and y == M-1 and count<=T :
            return min(count,result)
        count +=1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and  0 <= ny< M and not visited[nx][ny] :
                if graph[nx][ny] == 0 :
                    que.append([nx,ny,count])
                    visited[nx][ny] = True
                    
                elif graph[nx][ny]==2  :
                    que.append([nx,ny,count])
                    visited[nx][ny] = True
                    result = min(result, (count + abs(N-nx-1) + abs(M-ny-1)))

    if result != 10000000:
        return result

    return "Fail"    
                
input = sys.stdin.readline
N,M,T = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited =[[False] * M for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
print(bfs())

