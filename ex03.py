import sys
from collections import deque

def z_game():
    # 동 남 서 북
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    snail = deque()
    snail.append([0,0])
    now_direc = 0
    time = 0
    while 1:
        a,b = snail[-1]
        if time in rule:
            direc = rule[time]
            if direc == "D":
                now_direc = (now_direc + 4 + 1) % 4
            elif direc == "L":
                now_direc = (now_direc + 4 - 1) % 4
        nx = a + dx[now_direc]
        ny = b + dy[now_direc]
        # 벽에 부딛힌경우
        if nx<0 or ny<0 or nx>=N or ny>=N:
            return time + 1
        # 자기 몸에 부딛힌 경우
        if [nx,ny] in snail:
            return time + 1
        # 사과를 만난경우
        if graph[nx][ny] == "*":
            graph[nx][ny] = 0
            snail.append([nx,ny])
        else:
            snail.append([nx,ny])
            snail.popleft()
        time += 1

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apple = []
for _ in range(K):
    r,c = map(int,sys.stdin.readline().split())
    apple.append([r-1,c-1])
L = int(sys.stdin.readline())
rule = {}
for _ in range(L):
    X,C = map(str,sys.stdin.readline().split())
    rule[int(X)] = C

graph = [[0]*N for _ in range(N)]
for ap in apple:
    x,y = ap
    # 사과
    graph[x][y] = "*"

result = z_game()
print(result)