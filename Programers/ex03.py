from collections import deque
from hmac import new
from itertools import permutations
import re
q = deque()
n = 8
edges = [[0,1],[1,2],[2,3],[4,0],[5,1],[6,1],[7,2],[7,3],[4,5],[5,6],[6,7]]
k = 4
a = 0
b = 3

graph = [[] for _ in range(n)]

check_dic = {}
for e in edges:
    a1,b1 = e
    graph[a1].append(b1)
    graph[b1].append(a1)
    check_dic[str(a1)+str(b1)] = 0
result = []
print(graph)

for k1 in range(k+1):
    case = list(permutations(list(range(n)),k1+1))
    for c in case:
        if c[0] == a and c[-1]==b:
            flag = True
            for i in range(len(c)-1):
                if c[i] not in graph[c[i+1]]:
                    # print(c)
                    flag = False
                    break
            if flag and c not in result:
                result.append(c)
    
new_graph = [[] for _ in range(n)]

for r in result:
    for idx in range(len(r)-1):
        if r[idx+1] not in new_graph[r[idx]]:
            new_graph[r[idx]].append(r[idx+1])
answer = 0 
for cnt in new_graph:
    answer += len(cnt)
print(answer)













# q = deque()
# q.append([a,0,str(a)])
# while q:
#     x,dist,route = q.popleft()
#     if x == b and route not in result:
#         result.append(route)
#     for i in graph[x]:
#         if not visited[i] and dist <= 4:
#             visited[i] = True
#             q.append([i,dist,route+str(i)])
#     print(q)
#     print(visited)
