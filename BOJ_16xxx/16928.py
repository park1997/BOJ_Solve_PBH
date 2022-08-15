# 뱀과 사다리 게임
from collections import deque
import sys
N,M = map(int,sys.stdin.readline().split())
s = {}
b = {}
visited = [False]*101
graph = [0]*101
graph[1] = 0
for _ in range(N):
    a1,a2 = map(int,sys.stdin.readline().split())
    s[a1] = a2
for _ in range(M):
    a1,a2 = map(int,sys.stdin.readline().split())
    b[a1] = a2
q = deque()
q.append(1)
visited[1] = True
while q:
    # print(q)
    s1 = q.popleft()
    visited[s1] = True
    for j in range(1,7):
        ns = s1 + j 
        if ns <= 100 and not visited[ns]:
            if ns in s and not visited[s[ns]]:
                q.append(s[ns])
                visited[s[ns]] = True
                visited[ns] = True
                graph[ns] = graph[s1] + 1
                graph[s[ns]] = graph[s1] + 1
            if ns in b and not visited[b[ns]]:
                q.append(b[ns])
                visited[b[ns]] = True
                visited[ns] = True
                graph[ns] = graph[s1] + 1
                graph[b[ns]] = graph[s1] + 1
            if ns not in s and ns not in b:
                graph[ns] = graph[s1] + 1
                visited[ns] = True
                q.append(ns)
print(graph[100])
'''
2 1
2 60
30 98
65 25
'''
