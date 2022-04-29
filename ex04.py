import sys
from collections import deque
def main():

    def visit(start):
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        q = deque()
        visited = [[-1]*N for _ in range(N)]
        visited[start[0]][start[1]] = 0
        q.append(start)
        while q:
            a,b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if nx>=0 and ny>=0 and nx<N and ny<N and visited[nx][ny] == -1 and graph[nx][ny] != 1:
                    visited[nx][ny] = visited[a][b] + 1
                    q.append([nx,ny])
        return visited
        
    def check_distance(visited,arrival):
        for ar in arrival:
            ar.append(visited[ar[0]][ar[1]])
        arrival = list(sorted(arrival,key=lambda x : (-x[-1],-x[0],-x[1])))
        return arrival
        

    N,M,F = map(int,sys.stdin.readline().split())
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    driver = [0,0]
    a,b = map(int,sys.stdin.readline().split())
    driver[0] = a - 1
    driver[1] = b - 1
    arrival = []
    for _ in range(M):
        a,b,c,d = map(int,sys.stdin.readline().split())
        arrival.append([a-1,b-1,c-1,d-1])
    
    while arrival:
        visited = visit(driver)
        arr = check_distance(visited,arrival)
        arrival = [a[:] for a in arr]
        px,py,ax,ay,dist1 = arrival.pop()
        for t in arrival:
            t.pop()
        visited = visit([px,py])
        dist2 = visited[ax][ay]
        driver = [ax,ay]
        if dist1 == -1 or dist2 == -1:
            F = -1
            break
        F -= dist1
        if F < 0 :
            break
        F -= dist2
        if F < 0:
            break
        F += dist2 * 2
    
    if F<0:
        print(-1)
    else:
        print(F)





if __name__ == '__main__':
    main()