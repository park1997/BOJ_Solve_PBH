import sys
import heapq
def Djikstra(start):
    global m, n, r
    distance = [int(1e9)] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q,[0,start])
    while q:
        dis, now_node = heapq.heappop(q)
        if dis > m:
            continue
        if distance[now_node] < dis:
            continue
        for next_node, d in graph[now_node]:
            new_dis = dis + d
            if new_dis <= m and new_dis < distance[next_node]:
                distance[next_node] = new_dis
                heapq.heappush(q,[new_dis,next_node])
    return distance

n,m,r = map(int,sys.stdin.readline().split())
items = list(map(int,sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a,b,l = map(int,sys.stdin.readline().split())
    graph[a].append([b,l])
    graph[b].append([a,l])
result = -1
for node in range(1,n+1):
    d = Djikstra(node)
    temp_result = 0
    for idx, i in enumerate(d):
        if idx == 0:
            continue
        if i <= m:
            temp_result += items[idx-1]
    if temp_result > result:
        result = temp_result
print(result)
