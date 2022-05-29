import heapq
# from collections import deque
def solution(n, paths, gates, summits):
    def bfs(summits,gates):
        q = []
        for s in gates:
            visited = [0] * (n+1)
            visited[s] = 1
            heapq.heappush(q,[0,s,visited])
        while q:
            inten,now_node,now_visited = heapq.heappop(q)
            if now_node in summits:
                return [now_node,inten]
            for next_node,now_inten in graph[now_node]:
                real_inten = inten
                if now_visited[next_node]:
                    continue
                if next_node in gates:
                    continue
                if real_inten < now_inten:
                    real_inten = now_inten
                new_visited = [n for n in now_visited]
                new_visited[next_node] = 1
                heapq.heappush(q,[real_inten,next_node,new_visited])


    graph = [[] for _ in range(n+1)]
    for a,b,inten in paths:
        graph[a].append([b,inten])
        graph[b].append([a,inten])
    r = bfs(summits,gates)

    return r
n = 7
paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]

gates = [3,7]
summits = [1,5]
ans = solution(n, paths,gates, summits)
print(ans)


# 산봉우리가 많으면 산봉우리부터, 출발지가 많으면 출발지 부터 