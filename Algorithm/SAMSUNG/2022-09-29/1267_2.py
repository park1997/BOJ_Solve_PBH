T = 10
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    T = list(map(int, input().split()))
    count = V
    for i in range(E):
        a = T[2 * i]
        b = T[(2 * i) + 1]
        graph[b].append(a)
    result = []
    while count:
        for i in range(1, V):
            if not visited[i]:
                for j in graph[i]:
                    if visited[j]:
                        break
                else:
                    visited[i] = False
                    result.append(i)
                    count -= 1
    print('#{} '.format(test_case), end='')
    print(*result)