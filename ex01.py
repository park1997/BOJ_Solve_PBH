import sys
from collections import deque
def bfs(start):
    global N
    distance = [int(1e9)] * (N+1)
    distance[start] = 0
    q = deque()
    q.append([start,0])
    while q:
        s,d = q.popleft()
        if distance[s] < d:
            continue
        for node,dis in graph[s]:
            now_dis = dis + d
            if distance[node] > now_dis:
                distance[node] = now_dis
                q.append([node,now_dis])
    return distance


N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b,d = map(int,sys.stdin.readline().split())
    graph[a].append([b,d])
    graph[b].append([a,d])

d = bfs(1)
d2 = bfs(d.index(max(d[1:])))
print(max(d2[1:]))