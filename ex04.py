from collections import deque
from itertools import combinations


def bfs(start,end,t):
    global result
    visited = [[[0]*N for _ in range(N)] for _ in range(2)]
    q = deque()
    q.append([start[0],start[1],t])
    visited[t][start[0]][start[1]] = 1
    while q:
        a,b,c = q.popleft()
        print(q,a,b)
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<N:
                if visited[c][nx][ny] !=0 and ord(graph[a][b])<ord(graph[nx][ny]):
                    print(a,b,"->",nx,ny)
                    if visited[c][nx][ny] < visited[c][a][b] + 1:
                        visited[c][nx][ny] = visited[c][a][b] + 1
                        q.append([nx,ny,c])
                elif visited[c][nx][ny] == 0 and ord(graph[a][b])>=ord(graph[nx][ny]) and c == 0:
                    q.append([nx,ny,1])
                    visited[1][nx][ny] = visited[c][a][b] + 1
                elif visited[c][nx][ny] == 0 and ord(graph[a][b])<ord(graph[nx][ny]):
                    q.append([nx,ny,c])
                    visited[c][nx][ny] = visited[c][a][b] + 1
                if [nx,ny] == end:
                    for v in visited:
                        for i in v:
                            print(i)
                        print()
                    return
        for v in visited:
            for i in v:
                print(i)
            print()



N = int(input())
graph = [list(map(str,input().split())) for _ in range(N)]
s_to_e = [[i,j] for i in range(N) for j in range(N)]


combi = list(combinations(s_to_e,2))
dx = [0,1,0,-1]
dy = [1,0,-1,0]
result = -1
for c in combi:
    start = c[0]
    end = c[1]
    # bfs(start,end,0)
bfs([0,0],[4,4],0)
print(result)




'''
5
A B C F F
F F D E F
F F F F F
C B A G H
D E F G H

4
A B C D
G F E D
H I J K
O N M L

3
A B C
E D C
F G H
'''