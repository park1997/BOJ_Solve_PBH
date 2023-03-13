from collections import deque
start, end = map(int, input().strip().split())
def bfs(s):
    queue = deque()
    queue.append([s, 0])
    visited.append(s)
    while queue:
        u, t = queue.popleft()
        if u == end:
            return t
        for new_u in [u * 2, u - 1, u + 1]:
            if not visited[new_u]:
                if new_u == (u * 2):
                    queue.append([new_u, t])
                    visited[new_u] = True
                else:
                    queue.append([new_u, t + 1])
                    visited[new_u] = True
visited = [False] * (100001)
result = bfs(start)
print(result)