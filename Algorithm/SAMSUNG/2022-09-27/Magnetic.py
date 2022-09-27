def findCluster():
    global graph
    result = 0
    for j in range(N):
        flag = False
        for i in range(N):
            if graph[i][j] == 1:
                flag = True
            elif graph[i][j] == 2 and flag:
                result += 1
                flag = False
    return result
T = 10
for test_case in range(1, T + 1):
    f = False
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    result = findCluster()
    print("#{} {}".format(test_case,result))