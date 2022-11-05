import heapq
from collections import defaultdict
from mailbox import MH
graph = {}
check_node = []
distance_graph = {}
def init(N, sCity, eCity, mCost):
    global graph, check_node, distance_graph
    check_node = []
    distance_graph = {}
    graph = defaultdict(list)
    for i in range(N):
        s, e, c = sCity[i], eCity[i], mCost[i]
        graph[s].append([c,e])

    return len(graph)

def add(sCity, eCity, mCost):
    global graph, check_node
    graph[sCity].append([mCost, eCity])
    check_node.append(sCity)
    check_node.append(eCity)


def cost(mHub):
    global graph, check_node, distance_graph
    def Djikstra(mh):
        q = []
        heapq.heappush(q, [0, mh])
        distance = {}
        for g in graph:
            distance[g] = int(1e9)
        distance[mh] = 0
        while q:
            cur_dis, cur_node = heapq.heappop(q)
            if distance[cur_node] < cur_dis:
                continue
            for now_dis, now_node in graph[cur_node]:
                new_distance = now_dis + cur_dis
                if new_distance < distance[now_node]:
                    distance[now_node] = new_distance
                    heapq.heappush(q, [new_distance, now_node])
        return distance
    if mHub not in distance_graph:
        distance_graph[mHub] = {}
        for g in graph:
            distance_graph[mHub][g] = Djikstra(g)
    else:
        if len(check_node) != 0:
            for cn in check_node:
                distance_graph[mHub][cn] = Djikstra(cn)
                # print(cn, Djikstra(cn))
        else:
            pass
    ans = 0
    for d in distance_graph[mHub]:
        temp_distance = distance_graph[mHub][d]
        if d != mHub:
            ans += temp_distance[mHub]
        else:
            for node in temp_distance:
                ans += temp_distance[node]
    # print(check_node)
    # check_node = []
    # for d in distance_graph:
    #     print(d)
    #     for k in distance_graph[d]:
    #         print(k,end="")
    #         print(distance_graph[d][k])
    #     print()
    # print("*"*10)


    # ans = 0
    # for mh in graph:
    #     temp_distance = Djikstra(mh)
    #     if mh != mHub:
    #         ans += temp_distance[mHub]
    #     else:
    #         for td in temp_distance:
    #             ans += temp_distance[td]
    return ans