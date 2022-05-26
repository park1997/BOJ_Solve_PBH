import sys
import heapq
def monkey(graph):
    dx = [-1,-2,-2,-1,1,2,2,1]
    dy = [-2,-1,1,2,2,1,-1,-2]
    dx2 = [0,0,1,-1]
    dy2 = [1,-1,0,0]
    q = []
    heapq.heappush(q,[0,0,0,0])
    visited = [[False]*H for _ in range(W)]
    visited[0][0] = True
    while q:
        print(q)
        d,k,a,b = heapq.heappop(q)
        if [a,b] == [W-1,H-1]:
            return d
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<W and ny<H and not visited[nx][ny] and graph[nx][ny] != 1:
                
                heapq.heappush(q,[d+1,k+1,nx,ny])
                
                visited[nx][ny] = True
    return -1

K = int(sys.stdin.readline())
W, H = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(W)]

r = monkey(graph)
print(r)


