import sys
from collections import deque

def bfs(n):
    global k
    q = deque()
    count = 0
    q.append([count, n])
    visited[n] = True

    if n == k:
        return count

    while q:

        count, subin_location = q.popleft()
        print(count, subin_location)
        local_count = 0

        teleportation = subin_location * 2
        minus_1 = subin_location - 1
        plus_1 = subin_location + 1
        
        
        if teleportation == k:
            return count

        if minus_1 == k:
            local_count = count + 1
            return local_count

        if plus_1 == k:
            local_count = count + 1
            return local_count

        if 0 <= teleportation <= 100000 and visited[teleportation] == False:
            local_count = count
            q.append([local_count, teleportation])
            visited[teleportation] = True

        if 0 <= minus_1 <= 100000 and visited[minus_1] == False:
            local_count = count + 1
            q.append([local_count, minus_1])
            visited[minus_1] = True

        if 0 <= plus_1 <= 100000 and visited[plus_1] == False:
            local_count = count + 1
            q.append([local_count, plus_1])
            visited[plus_1] = True

n, k = map(int, sys.stdin.readline().split())

visited = [False] * 100001

result = bfs(n)
print(result)