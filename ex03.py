import sys
import heapq
def prim():
    result = 0
    q = []
    heapq.heappush(q, [0, 0])
    visited = [False] * N
    while q:
        cur_dis, cur_node = heapq.heappop(q)
        if visited[cur_node]:
            continue
        result += cur_dis
        visited[cur_node] = True
        for d, n in graph[cur_node]:
            if not visited[n]:
                heapq.heappush(q, [d, n])
    return result

N = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
points = []
for i in range(N):
    a,b,c = map(int, sys.stdin.readline().split())
    points.append([a, b, c, i])
px = [p[:] for p in points]
py = [p[:] for p in points]
pz = [p[:] for p in points]
px.sort(key = lambda x : x[0])
py.sort(key = lambda x : x[1])
pz.sort(key = lambda x : x[2])

for i in range(1, N, 1):
    x1, y1, z1, i1 = px[i - 1]
    x2, y2, z2, i2 = px[i]
    dis = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
    graph[i1].append([dis, i2])
    graph[i2].append([dis, i1])

    x1, y1, z1, i1 = py[i - 1]
    x2, y2, z2, i2 = py[i]
    dis = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
    graph[i1].append([dis, i2])
    graph[i2].append([dis, i1])

    x1, y1, z1, i1 = pz[i - 1]
    x2, y2, z2, i2 = pz[i]
    dis = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
    graph[i1].append([dis, i2])
    graph[i2].append([dis, i1])

result = prim()
print(result)