import heapq
from mailbox import MH
graph = {}
def init(N, sCity, eCity, mCost):
    global graph
    graph = {}
    for i in range(N):
        s, e, c = sCity[i], eCity[i], mCost[i]
        if s not in graph:
            graph[s] = [[c, e]]
        else:
            graph[s].append([c, e])
    return len(graph)

def add(sCity, eCity, mCost):
    global graph
    graph[sCity].append([mCost, eCity])


def cost(mHub):
    global graph
    q = []
    heapq.heappush(q, [0, mHub])
    print(mHub, len(graph))
    distance = [int(1e9)] * (len(graph) + 1)
    distance[mHub] = 0
    while q:
        cur_cost, cur_node = heapq.heappop(q)
        if distance[cur_node] < cur_cost:
            continue
        for now_cost, now_node in graph[cur_node]:
            new_distance = now_cost + cur_cost
            if new_distance < distance[now_node]:
                distance[now_node] = new_distance
                heapq.heappush(q, [new_distance, now_node])
    print(distance)
    print(sum(distance[1:]))
    return sum(distance[1:])