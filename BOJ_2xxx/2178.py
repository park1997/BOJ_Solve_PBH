# 미로탐색
from collections import deque
N, M = map(int, input().split())
miro = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    miro.append(list(input()))
q= deque()
q.append([0,0])
miro[0][0] = 1
while q:
    a, b = q.popleft()
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < N and 0 <= y < M and miro[x][y] == "1":
            q.append([x, y])
            miro[x][y] = miro[a][b] + 1
print(miro[N-1][M-1])