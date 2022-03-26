import sys
# import heapq
from collections import deque
def bfs():
    global graph, result
    check = {graph:0}
    # q = []
    # heapq.heappush(q,[0,graph])
    q = deque()
    q.append(graph)
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    while q:
        # cnt,g = heapq.heappop(q)
        g = q.popleft()
        if g == result:
            return check[g]
        z = g.index("0")
        x = z //3
        y = z % 3
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >=0 and ny>=0 and nx<3 and ny<3:
                new_z = nx * 3 + ny
                new_g = list(g)
                temp = new_g[z]
                new_g[z] = new_g[new_z]
                new_g[new_z] = temp
                new_g = "".join(new_g)
                if new_g not in check:
                    check[new_g] = check[g] + 1
                    # heapq.heappush(q,[cnt+1,new_g])
                    q.append(new_g)
    return -1

result = "123456780"
graph = ""
for i in range(3):
    graph += "".join(list(map(str,sys.stdin.readline().split())))
print(bfs())
