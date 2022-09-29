def dfs(start):
    visited[start] = True
    result.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(i)

# 정점, 간선
V, E = 7, 8
T= [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
graph = [[] for _ in range(V + 1)]
for i in range(E):
    a = 2 * i
    b = a + 1
    graph[T[a]].append(T[b])
    graph[T[b]].append(T[a])
visited = [False] * (V + 1)
result = []
dfs(1)
print(*result,sep="-")