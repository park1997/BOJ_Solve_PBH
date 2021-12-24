from collections import deque
import sys
N,M,K,X = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
visited = [False]*(N+1)
distance = [0]*(N+1)
q = deque()
q.append(X)
visited[X] = True
while q:
    now = q.popleft()
    for i in graph[now]:
        if not visited[i]:
            visited[i] = True
            distance[i] =  distance[now]+1
            q.append(i)
flag = True
for idx,i in enumerate(distance):
    if i == K:
        flag = False
        print(idx)
if flag:
    print(-1)
