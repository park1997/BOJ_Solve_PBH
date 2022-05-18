import sys
def bfs(start):
    


    return


N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(N):
    a,b,d = map(int,sys.stdin.readline().split())
    graph[a].append([b,d])
    graph[b].append([a,d])

bfs(1)