# 마라톤
from itertools import combinations
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
total_dis = 0
for i in range(N):
    if i+1!=N:
        total_dis += abs(graph[i][0]-graph[i+1][0]) + abs(graph[i][1]-graph[i+1][1])
    # else:
    #     total_dis += abs(graph[i][0]-graph[0][0]) + abs(graph[i][1]-graph[0][1])

result = int(1e9)
for i in range(1,N-1):
    t1 = total_dis
    temp = 0
    t1 -= abs(graph[i-1][0]-graph[i][0]) + abs(graph[i-1][1]-graph[i][1]) 
    t1 -= abs(graph[i+1][0]-graph[i][0]) + abs(graph[i+1][1]-graph[i][1]) 
    t1 += abs(graph[i+1][0]-graph[i-1][0]) + abs(graph[i+1][1]-graph[i-1][1])
    
    if result>t1:
        result = t1
print(result)



