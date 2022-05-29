# 백준 1197
import sys
import heapq
def spanning_tree(s):
    global graph, visited
    q = []
    heapq.heappush(q,[0,s])
    v_cnt = 0
    result = 0
    while v_cnt < V:
        dis,a = heapq.heappop(q)
        if visited[a]:
            continue
        visited[a] = True
        result += dis
        v_cnt += 1
        for i,d in graph[a]:
            if not visited[i]:
                heapq.heappush(q,[d,i])
    return result 

V,E = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
visited = [False] * (V+1)
r = spanning_tree(1)
print(r)

'''
3 3
1 2 1
2 3 2
1 3 3
'''