def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    print(N,M)
    prefix_graph = [[0]*(M+1) for _ in range(N+1)]
    # for i in range(1,N):
    #     for j in range(1,M):
    #         prefix_graph[i][j] = board[i-1][j-1]
    
    # for i in range(1,N):
    #     for j in range(1,M):
    #         prefix_graph[i][j] = prefix_graph[i-1][j] + prefix_graph[i][j-1] - prefix_graph[i-1][j-1] + prefix_graph[i][j]

    # for p in prefix_graph:
    #     print(p)
    
    for p in prefix_graph:
        print(p)
    print()
    for b in board:
        print(b)
    for type,r1,c1,r2,c2,degree in skill:
        if type == 1:
            prefix_graph[r1][c1] -= degree
            prefix_graph[r1][c2+1] += degree
            prefix_graph[r2+1][c1] += degree
            prefix_graph[r2+1][c2+1] -= degree
        elif type == 2:
            prefix_graph[r1][c1] += degree
            prefix_graph[r1][c2+1] -= degree
            prefix_graph[r2+1][c1] -= degree
            prefix_graph[r2+1][c2+1] += degree
    
    for i in range(N-1):
        for j in range(M-1):
            prefix_graph[i][j+1] += prefix_graph[i][j]
    
    for j in range(M-1):
        for i in range(N-1):
            prefix_graph[i+1][j] += prefix_graph[i][j]
    
    for i in range(M-1):
        for j in range(N-1):
            prefix_graph[i][j] += board[i][j]
    
    for p in prefix_graph:
        print(p)




    return answer


board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]



ans = solution(board,skill)
print(ans)