import sys
from collections import deque
def bfs(s):
    global cnt
    dx = [2,1,-1]
    visited[s] = 0
    q = deque()
    q.append(s)
    while q:
        a = q.popleft()
        if a == K:
            cnt += 1
        for i in range(3):
            if i ==0:
                nx = a * dx[i]
            else:
                nx = a + dx[i]
            if nx >=0 and nx <= 100000 :
                if visited[nx] == -1 or visited[nx] >= visited[a] + 1:
                    visited[nx] = visited[a] + 1
                    q.append(nx)
                
                
    
N,K = map(int,sys.stdin.readline().split())
visited = [-1]*(100001)
cnt = 0
bfs(N)
print(visited[K])
print(cnt)
