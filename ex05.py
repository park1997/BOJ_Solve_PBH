import heapq
import sys
def djikstra(start):
    q = []
    heapq.heappush(q, [0, start])
    while q:
        dis, node = heapq.heappop(q)
            continue
        for now_dis, now_node in graph[node]:
            new_dis = now_dis + dis
            if distance[now_node] > new_dis:
                distance[now_node] = new_dis
                heapq.heappush(q, [new_dis, now_node])
T = int(input())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    graph = {}
    for __ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        if [a, b] == [g, h] or [a, b] == [h, g]:
            if a not in graph:
                graph[a] = [[d - 0.1 , b]]
            else:
                graph[a].append([d - 0.1, b])
            if b not in graph:
                graph[b] = [[d - 0.1, a]]
            else:
                graph[b].append([d - 0.1, a])
            continue
        if a not in graph:
            graph[a] = [[d, b]]
        else:
            graph[a].append([d, b])
        if b not in graph:
            graph[b] = [[d, a]]
        else:
            graph[b].append([d, a])
    distance = [int(1e9)] * (n + 1)
    distance[s] = 0
    djikstra(s)
    result = []
    for __ in range(t):
        x  = int(sys.stdin.readline().strip())
        if type(distance[x]) is float:
            result.append(x)
    result.sort()
    print(*result)
