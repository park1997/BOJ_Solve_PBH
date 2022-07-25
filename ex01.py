import sys
import heapq
def bfs(s):
    dx = [2,1,-1]
    q = []
    visited[s] = 0
    heapq.heappush(q,[visited[s],s])

    while q:
        dis,a = heapq.heappop(q)
        print(dis,s)
        if a == K:
            return dis
        for i in range(3):
            if i ==0 :
                nx = a * dx[i]
            else:
                nx = a + dx[i]
            if nx>=0 and nx<=100000 and visited[nx] == -1:
                if i ==0 :
                    visited[nx] = visited[a]
                    heapq.heappush(q,[visited[nx],nx])
                else:
                    visited[nx] = visited[a] + 1
                    heapq.heappush(q,[visited[nx],nx])



N,K = map(int,sys.stdin.readline().split())
visited = [-1]*(100001)
print(bfs(N))
