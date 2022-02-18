import sys
import heapq
def bfs(K):
    q = []
    heapq.heappush(q,(0,K))
    distance[K] = 0
    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue
        for v1,w1 in graph[now]:
            if distance[v1] > w1 + distance[now]:
                distance[v1] = w1 + distance[now]
                heapq.heappush(q,(distance[v1],v1))

V,E = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline())
distance = [int(1e9)]*(V+1)
visited = [False]*(V+1)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    # u노드에서 v노드까지 가는비용 w
    graph[u].append([v,w])
bfs(K)
for i in range(1,V+1):
    if distance[i] == int(1e9):
        print("INF")
    else:
        print(distance[i])