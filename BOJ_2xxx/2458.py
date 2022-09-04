# 키 순서
from collections import deque

def dfs1(s):
    global graph
    visited1[s] = True
    for i in graph1[s]:
        if not visited1[i]:
            visited1[i] = True
            dfs1(i)
def dfs2(s):
    global graph
    visited2[s] = True
    for i in graph2[s]:
        if not visited2[i]:
            visited2[i] = True
            dfs2(i)

N,M = map(int,input().split())
graph1 = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
order = [list(map(int,input().split())) for _ in range(M)]
for a,b in order:
    graph1[a].append(b)
for a,b in order:
    graph2[b].append(a)
visited=[False]*(N+1)
# bfs(1)
cnt = 0
for i in range(1,N+1):
    visited1=[False]*(N+1)
    visited2=[False]*(N+1)
    dfs1(i)
    dfs2(i)
    if sum(visited1)+sum(visited2) -1 == N:
        cnt +=1
print(cnt)
