import sys
import heapq
def Djikstra(S,D):
    global visited
    q = []
    visited[S] = True
    distance[S] = 0
    r = [int(1e9)]*2
    heapq.heappush(q,[0,S])
    while q:
        d,n = heapq.heappop(q)
        for node,dis in graph[n]:
            new_dis = d + dis
            if node == D:
                if r[0] > new_dis:
                    r[0] = new_dis
                elif r[1] > new_dis and new_dis!=r[0]:
                    r[1] = new_dis
            if new_dis < distance[node]:
                distance[node] = new_dis
                heapq.heappush(q,[new_dis,node])

    return r

    

while 1:
    N,M = map(int,sys.stdin.readline().split())
    if N==0 and M==0:
        break
    S,D = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        U,V,P = map(int,sys.stdin.readline().split())
        graph[U].append([V,P])
    visited = [False]*(N+1)
    distance = [int(1e9)]*(N+1)
    result = Djikstra(S,D)
    print(result)




