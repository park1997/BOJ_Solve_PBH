from collections import deque

N, M, energy = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
sx, sy = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(M)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(sx,sy):
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    q.append([sx,sy])
    visited[sx][sy] = 0
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx>=0 and ny>=0 and nx<N and ny<N :
                if graph[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[a][b] + 1
                    q.append([nx,ny])
    return visited

def distance(visited,people):
    # print(people)
    for idx,p in enumerate(people):
        px,py,ax,ay = p
        people[idx].append(visited[px-1][py-1])
    # print(people)
    # people = list(sorted(people , key = lambda x : (-x[4],-x[0],-x[1])))
    people.sort(key=lambda x: (-x[4], -x[0], -x[1]))
    # print(people)


def solve(sx,sy):
    global energy
    while people:
        visited = bfs(sx-1,sy-1)
        distance(visited,people)
        px,py,ax,ay,dist = people.pop()
        for temp in people:
            temp.pop()
        visited = bfs(px-1,py-1)
        dist2 = visited[ax-1][ay-1]
        sx,sy = ax,ay
        if dist == -1 or dist2 == -1:
            print(-1)
            return

        energy -= dist
        if energy<0:
            break

        energy -= dist2
        if energy<0:
            break
        energy += dist2 * 2

    if energy<0:
        print(-1)
    else:
        print(energy)

solve(sx,sy)

'''
6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
'''