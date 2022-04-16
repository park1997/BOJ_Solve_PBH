import sys
import heapq
def Djikstra(start):
    q = []
    heapq.heappush(q,[0,start])
    distance[start] = 0
    while q:
        dis,node = heapq.heappop(q)
        # if distance[node] < dis:
        #     continue
        for n,d in graph[node]:
            new_d = dis + d
            if distance[n] > new_d:
                distance[n] = new_d
                heapq.heappush(q,[new_d,n])

V,E = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
distance = [int(1e9)]*(V+1)
Djikstra(start)
for i in range(1,len(distance)):
    if distance[i] != int(1e9):
        print(distance[i])
    else:
        print("INF")
