def reculsion(n, d, depth):
    global result

    if result <= d:
        return

    if depth == N-2:
        result = min(result, d+abs(A[2*n] - A[2]) + abs(A[2*n+1] - A[3]))
        return

    for i in range(2, N):
        if not visited[i]:
            visited[i] = True
            reculsion(i, d+abs(A[2*n] - A[2*i]) + abs(A[2*n+1] - A[2*i+1]), depth+1)
            visited[i] = False

T = int(input())
for test_case in range(1, T+1):
    N = int(input())+2
    A = list(map(int, input().split()))
    visited = [False for _ in range(N)]
    result = int(1e9)
    reculsion(0, 0, 0)
    print('#{} {}'.format(test_case, result))