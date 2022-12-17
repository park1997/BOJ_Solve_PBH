import sys
import heapq
def djikstra(start : int) -> None:
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        dis, node = heapq.heappop(q)
        if dis > distance[node]:
            continue
        for d, n in graph[node]:
            new_dis = d + dis
            if distance[n] > new_dis:
                heapq.heappush(q, [new_dis, n])
                distance[n] = new_dis


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, v = map(int, sys.stdin.readline().split())
    graph[a].append([v, b])
    # graph[b].append([v, a])
distance = [int(1e9)] * (N + 1)
start, end = map(int, sys.stdin.readline().split())
djikstra(start)
print(distance[end])
