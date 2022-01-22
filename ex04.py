from collections import deque
import sys
def bfs(s):
    global visited
    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i]==0:
                q.append(i)
                visited[i] = -visited[a]
            else:
                if visited[i]==visited[a]:
                    return False
    return True

K = int(input())
for i in range(K):
    V,E = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(E):
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    flag = False
    for i in range(1,V+1):
        if visited[i]==0:
            if not bfs(i):
                flag = True
                break

    if flag:
        print("NO")
    else:
        print("YES")
