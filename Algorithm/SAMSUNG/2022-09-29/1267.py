from collections import deque
def dfs(start):
    q = deque()
    q.append(start)
    while q:
        node = q.pop()
        
        if not visited[node]:
            visited[node] = True
            q.extend(graph[node])
            print(node)
        

T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    T = list(map(int, input().split()))
    graph = [[] for _ in range(V+1)]
    start = -1
    for i in range(E):
        a = 2 * i
        b = a + 1
        graph[T[b]].append(T[a])
        start = max(len(graph[T[b]]), start)
    print(graph)
    visited = [False] * (V + 1)
    q = deque()
    for s in range(1, V+1, 1):
        if not visited[s]:
            q.append(s)

