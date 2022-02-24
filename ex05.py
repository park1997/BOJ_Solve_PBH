import sys
import heapq
def Djikstra():
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = []
    heapq.heappush(q,[graph[0][0],0,0])
    visited[0][0] = graph[0][0]
    while q:
        dis,a,b = heapq.heappop(q)
        if [a,b] == [T-1,T-1]:
            return
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<T and ny<T:
                if visited[nx][ny] > dis + graph[nx][ny]:
                    visited[nx][ny] = dis + graph[nx][ny]
                    heapq.heappush(q,[visited[nx][ny],nx,ny])
                
i = 0
while 1:
    T = int(sys.stdin.readline())
    if T == 0:
        break
    i+=1
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(T)]
    visited = [[int(1e9)]*T for _ in range(T)]
    result = 0
    Djikstra()
    print("Problem {}: {}".format(i,visited[-1][-1]))

