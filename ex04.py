import sys

def wind(graph,start,direc,sand):
    global result
    dx, dy, rate, ax, ay = None, None, None, None, None
    a,b = start
    graph[a][b] = 0
    if direc == 0:
        dx = [-1,-2,-1,1,1,2,1,0,-1]
        dy = [0,0,1,1,0,0,-1,-2,-1]
        rate = [0.07,0.02,0.01,0.01,0.07,0.02,0.1,0.05,0.1]
        ax = 0
        ay = -1
    elif direc == 1:
        dx = [-1,0,0,1,2,1,0,0,-1]
        dy = [1,1,2,1,0,-1,-1,-2,-1]
        rate = [0.01,0.07,0.02,0.1,0.05,0.1,0.07,0.02,0.01]
        ax = 1
        ay = 0
    elif direc == 2:
        dx = [-1,-2,-1,0,1,1,2,1,-1]
        dy = [0,0,1,2,1,0,0,-1,-1]
        rate = [0.07,0.02,0.1,0.05,0.1,0.07,0.02,0.01,0.01]
        ax = 0
        ay = 1
    elif direc == 3:
        dx = [-2,-1,0,0,1,1,0,0,-1]
        dy = [0,1,1,2,1,-1,-1,-2,-1]
        rate = [0.05,0.1,0.07,0.02,0.01,0.01,0.07,0.02,0.1]
        ax = -1
        ay = 0
    spread = 0
    for i in range(9):
        nx = a + dx[i]
        ny = b + dy[i]
        r = rate[i]
        for_spread = int(sand * r)
        if nx>=0 and ny>=0 and nx<N and ny<N:
            graph[nx][ny] += for_spread
            spread += for_spread
        else:
            result += for_spread
            spread += for_spread
    nx2 = a + ax
    ny2 = b + ay
    if nx2>=0 and ny2>=0 and nx2<N and ny2<N:
        graph[nx2][ny2] += sand - spread
    else:
        result += sand - spread

    return graph


def tornado(graph):
    global N,result
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    mid = N //2
    start = [mid,mid]
    distance = []
    for i in range(1,N+1,1):
        for _ in range(2):
            distance.append(i)
    direc = 0
    a,b = start
    while 1:
        nx,ny = a,b
        for dis in distance:
            for _ in range(dis):
                nx += dx[direc]
                ny += dy[direc]
                sand = graph[nx][ny]
                if sand != 0:
                    graph = wind(graph,[nx,ny],direc,sand)
                if [nx,ny] == [0,0]:
                    return
            direc = (direc + 1) % 4

N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
result = 0

tornado(graph)
print(result)