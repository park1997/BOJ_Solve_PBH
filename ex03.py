from collections import deque

n, m, energy = map(int, input().split(' '))
graph = [list(map(int, input().split(' '))) for _ in range(n)]
sx, sy = map(int, input().split(' '))
people = [list(map(int, input().split(' '))) for _ in range(m)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy):
    visited = [[-1] * n for _ in range(n)]
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = 0
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] != 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[a][b] + 1
                    queue.append([nx, ny])
    return visited

def check_dist(visited, people):
    
    for idx,p in enumerate(people):
        px,py,ax,ay = p
        people[idx].append(visited[px - 1][py - 1])
    print(people)
    people.sort(key=lambda x: (-x[4], -x[0], -x[1]))
    print(people)

def solve(sx, sy):
    global energy
    while people:
        visitied = bfs(sx - 1, sy - 1)
        check_dist(visitied, people)
        p_x, p_y, ax, ay, dist = people.pop()
        
        for temp in people:
            temp.pop()
        
        visitied = bfs(p_x - 1, p_y - 1)
        dist2 = visitied[ax - 1][ay - 1]
        sx, sy = ax, ay

        if dist == -1 or dist2 == -1:
            print(-1)
            return

        energy -= dist
        if energy < 0:
            break

        energy -= dist2
        if energy < 0:
            break

        energy += dist2 * 2

    if energy < 0:
        print(-1)
    else:
        print(energy)


solve(sx, sy)