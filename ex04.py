import sys
import heapq

def prim(start):
    ans = 0
    q = []
    visited = [False] * (N + 1)
    heapq.heappush(q, [0, start, univ[start - 1]])
    while q:
        cur_dis, cur_node, cur_univ = heapq.heappop(q)
        if visited[cur_node]:
            continue
        ans += cur_dis
        visited[cur_node] = True
        for now_dis, now_node, now_univ in graph[cur_node]:
            if not visited[now_node] and cur_univ != now_univ:
                heapq.heappush(q, [now_dis, now_node, now_univ])
    return ans, visited

N, M = map(int, sys.stdin.readline().split())
univ = list(map(str, sys.stdin.readline().split()))
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, d = map(int, sys.stdin.readline().split())
    graph[u].append([d, v, univ[v - 1]])
    graph[v].append([d, u, univ[u - 1]])

result, visited = prim(1)
if sum(visited) == N:
    print(result)
else:
    print(-1)



