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
            # print(inten,now_node,now_visited)
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

    # answer = [int(1e9),int(1e9)]
    graph = [[] for _ in range(n+1)]
    # min_path = int(1e9)
    for a,b,inten in paths:
        graph[a].append([b,inten])
        graph[b].append([a,inten])
        # if inten < min_path:
        #     min_path = inten
    r = bfs(summits,gates)

    return r
n = 7
paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]

gates = [3,7]
summits = [1,5]
ans = solution(n, paths,gates, summits)
print(ans)


'''
테스트 1 〉 통과 (0.03ms, 10.2MB)
테스트 2 〉 통과 (0.03ms, 10.1MB)
테스트 3 〉 통과 (0.02ms, 10.2MB)
테스트 4 〉 통과 (0.01ms, 10.1MB)
테스트 5 〉 통과 (0.04ms, 10MB)
테스트 6 〉 통과 (0.31ms, 10.2MB)
테스트 7 〉 통과 (0.57ms, 10.3MB)
테스트 8 〉 통과 (0.41ms, 10.2MB)
테스트 9 〉 통과 (0.34ms, 10.1MB)
테스트 10 〉 통과 (1.67ms, 10MB)
테스트 11 〉 통과 (23.29ms, 10.2MB)
테스트 12 〉 통과 (2.81ms, 10.3MB)
테스트 13 〉 통과 (69.06ms, 14.1MB)
테스트 14 〉 실패 (2068.02ms, 51.4MB)
테스트 15 〉 실패 (시간 초과)
테스트 16 〉 실패 (시간 초과)
테스트 17 〉 실패 (시간 초과)
테스트 18 〉 실패 (시간 초과)
테스트 19 〉 통과 (776.63ms, 127MB)
테스트 20 〉 실패 (시간 초과)
테스트 21 〉 실패 (시간 초과)
테스트 22 〉 실패 (시간 초과)
테스트 23 〉 실패 (시간 초과)
테스트 24 〉 실패 (시간 초과)
테스트 25 〉 실패 (시간 초과)
'''