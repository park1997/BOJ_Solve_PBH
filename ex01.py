from collections import deque
start, end = map(int, input().split())
def bfs(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1
    while queue:
        u = queue.popleft()
        if u == end:
            return visited[u]
        for new_u in [u * 2, u - 1, u + 1]:
            if 0 <= new_u <= 100000: 
                if visited[new_u] == 0:
                    if new_u == (u * 2):
                        queue.append(new_u)
                        visited[new_u] = visited[u]
                    else:
                        queue.append(new_u)
                        visited[new_u] = visited[u] + 1
visited = [0] * (100001)
result = bfs(start)
print(result - 1)
