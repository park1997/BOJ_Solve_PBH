import sys
import heapq
def prim(start):
    global n
    q = []
    heapq.heappush(q, [0, start])
    result = 0
    visited = [False] * (n)
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

n = int(sys.stdin.readline())
point = []
graph = []
for _ in range(n):
    a, b = map(float, sys.stdin.readline().split())
    point.append([a,b])
    graph.append([])

for i in range(n - 1):
    for j in range(i, n, 1):
        if i == j:
            continue
        start = point[i]
        end = point[j]
        dis = ((abs(start[0] - end[0]) ** 2) + (abs(start[1] - end[1])) ** 2) ** (1/2)
        graph[i].append([dis, j])
        graph[j].append([dis, i])

result = prim(0)
print("{:.2f}".format(result))


