# Gravity
N,M = map(int,input().split())
graph =[list(input()) for _ in range(N)]

for j in range(M):
    while 1:
        cnt = 0
        for i in range(N):
            if i+1<N:
                if graph[i][j] == "o" and graph[i+1][j]==".":
                    temp = graph[i][j]
                    graph[i][j] = graph[i+1][j]
                    graph[i+1][j] = temp
                    cnt +=1
        if cnt == 0:
            break
                

for i in graph:
    print("".join(i))