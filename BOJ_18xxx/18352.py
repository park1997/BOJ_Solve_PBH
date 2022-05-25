# 특정 거리의 도시 찾기
from collections import deque
import sys
N,M,K,X = map(int,sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
distance = [0]*(N+1)
visited = [False]*(N+1)

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)

def bfs(s):
    q = deque([s])
    visited[s] = True
    distance[s] = 0
    flag = True

    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now]+1
    for idx,i in enumerate(distance):
        if i == K:
            flag = False
            print(idx,end=" ")
    if flag:
        print(-1)
bfs(X)