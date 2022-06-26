import sys
N, M, B = map(int,sys.stdin.readline().split())
graph = []
h_max = 0
h_min = int(1e9)
for i in range(N):
    l = list(map(int,sys.stdin.readline().split()))
    temp_max = max(l)
    temp_min = min(l)
    h_max = max(h_max,temp_max)
    h_min = min(h_min,temp_min)
    graph.append(l)
print(l)
print(h_max,h_min)
result = []
for height in range(h_min,h_max+1):
    time = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] < height:
                time += (graph[i][j] - height) * 2
            elif graph[i][j] > height:
                


