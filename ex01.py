from collections import deque
import heapq
def solution(n, start, end, roads, traps):
    def change_graph(graph,t):
        new_graph = [[] for _ in range(n+1)]
        for i,gra in enumerate(graph):
            for g in gra:
                node,distance = g
                if i == t or node == t:
                    new_graph[node].append([i,distance])
                else:
                    new_graph[i].append([node,distance])
        return new_graph
    
    
    def bfs(start,end,graph):
        q = []
        heapq.heappush(q,[0,start,graph])
        cnt = 0
        while q:
            cnt += 1
            print(q)
            distance,node,now_graph = heapq.heappop(q)
            print(node,distance,now_graph)
            if node == end:
                return distance
            for no,dis in now_graph[node]:
                print(dis,no)
                if no in traps:
                    graph = change_graph(graph,no)
                    heapq.heappush(q,[distance + dis, no, graph])
                else:
                    heapq.heappush(q,[distance + dis, no, now_graph])
            if cnt == 10:
                break
                    
    answer = 0
    graph = [[] for _ in range(n+1)]
    for r in roads:
        a,b,c = r
        graph[a].append([b,c])
    
    answer = bfs(start,end,graph)
    
    return answer

a = solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3])
print(a)
