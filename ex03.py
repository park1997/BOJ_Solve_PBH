def solution(v1, v2, a, b):
    node_num = len(v1)
    graph = [[] for _ in range(1001)]
    for i in range(node_num):
        start = v1[i]
        end = v2[i]
        graph[start].append(end)
        graph[end].append(start)
    # 친구 조사
    case = {}
    for i in range(1001):
        case[i] = 0
    for n in graph[a]:
        case[n] += 1
    for n in graph[b]:
        case[n] += 1
    friends = [c for c in case if case[c] >= 2]
    if len(friends) == 0:
        return -1
    r = [[len(graph[f]), f] for f in friends]
    r = sorted(r, key = lambda x : (x[0], x[1]))
    return r[0][1]



# v1 = [0,0,1,2,2]
# v2 = [1,2,3,3,4]
# a = 0
# b = 3

# v1 = [0,0,1,2,3]
# v2 = [1,2,3,3,4]
# a = 0
# b = 4

# v1 = [998, 1000]
# v2 = [1000, 999]
# a = 998
# b = 999
print(solution(v1, v2, a, b))