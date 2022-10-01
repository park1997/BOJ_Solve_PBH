import sys
from heapq import heappush,heappop

def direction(x,y,n):

    if n == 0:
        return x+1,y
    elif n == 1:
        return x-1,y
    elif n == 2:
        return x,y+1
    else:
        return x,y-1

def reverse(n):
    if n == 0:
        return 1

    elif n == 1:
        return 0

    elif n == 2:
        return 3

    else:
        return 2


input = sys.stdin.readline

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
door = []
h = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited = [[[0]*N for _ in range(N)] for _ in range(4)]
flag = False
for i in range(N):
    for j in range(N):
        if arr[i][j] == '#':
            if not flag:
                start_x,start_y = i,j
                flag = True
            else:
                end_x,end_y = i,j




cnt = 0
for dir in range(4):
    a,b = start_x+dx[dir],start_y+dy[dir]

    if 0 <= a < N and 0 <= b < N and not visited[dir][a][b] and arr[a][b] != '*':
        
        visited[dir][a][b] = 1
        heappush(door,[0,a,b,dir])

        if arr[a][b] == '.':
            heappush(door,[cnt,a,b,dir])
            visited[dir][a][b] = 1
        else:
            for i in range(4):
                if reverse(dir) == i:
                    continue 
                if i == dir:
                    heappush(door,[cnt,a,b,dir])
                else:
                    heappush(door,[cnt+1,a,b,i])
            visited[dir][a][b] = 1    


# ===========================================================================

answer = float('inf')
while door:

    cnt,x,y,dir = heappop(door)
    
    if [x,y]==[end_x,end_y]:
        answer = cnt
        break
        
    a,b = direction(x,y,dir)
    
    if 0 <= a < N and 0 <= b < N and not visited[dir][a][b] and arr[a][b] != '*':
        
        if arr[a][b] == '.':
            heappush(door,[cnt,a,b,dir])
            visited[dir][a][b] = 1
        else:
            for i in range(4):
                if reverse(dir) == i:
                    continue 
                if i == dir:
                    heappush(door,[cnt,a,b,dir])
                else:
                    heappush(door,[cnt+1,a,b,i])
            visited[dir][a][b] = 1

print(answer)




