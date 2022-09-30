T = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    T = list(map(int, input().split()))
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    count = V
    for i in range(E):
        a = T[2 * i]
        b = T[2 * i + 1]
        graph[b].append(a)
    result = []
    count = V
    while count:
        for i in range(1, V + 1, 1):
            if not visited[i]:
                flag = True
                for j in graph[i]:
                    if not visited[j]:
                        flag = False
                        break
                if flag:
                    result.append(i)
                    count -= 1
                    visited[i] = True
    print("#{} ".format(test_case), end = "")
    print(*result)


"[[], [4], [1], [2], [], [1, 8], [5, 7], [2], [], [8]]"