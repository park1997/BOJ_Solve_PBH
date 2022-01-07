import sys
sys.setrecursionlimit(10**9)
def dfs(start):
    global visited
    global graph
    visited[start] = True
    for k in graph[start]:
        if not visited[k]:
            dfs(k)

N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        cnt +=1
print(cnt)