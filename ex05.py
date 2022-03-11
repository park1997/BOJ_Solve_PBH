import sys
import heapq
def Djikstra(s):
    global n
    distance = [int(1e9)]*(n+1)
    q = []
    heapq.heappush(q,[0,s])
    distance[s] = 0
    while q:
        dis,a = heapq.heappop(q)
        for node,d in graph[a]:
            new_dis = dis + d
            if new_dis < distance[node]:
                distance[node] = new_dis
                heapq.heappush(q,[new_dis,node])
                result[node][s] = a

n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
result = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b,t = map(int,sys.stdin.readline().split())
    graph[a].append([b,t])
    graph[b].append([a,t])

for i in range(1,n+1):
    Djikstra(i)

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print("-",end=" ")
        else:
            print(result[i][j],end=" ")
    print()