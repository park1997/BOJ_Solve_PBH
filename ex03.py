import sys
from collections import deque
sys.setrecursionlimit(100000)
def main():
    
    def fish_go(graph):
        s_graph = [g[:] for g in graph]
        fish = []
        for gr in s_graph:
            for g in gr:
                fish.append(g)
        fish = sorted(fish,key = lambda x : x[2])
        q = deque(fish)
        while q:
            n_x, n_y, n_num, n_direc = q.popleft()
            if n_num == int(1e9):
                break
            while 1:
                n_x += dx[n_direc]
                n_y += dy[n_direc]
                # 그래프를 벗어나는경우 => 방향 전환
                if n_x<0 or n_y<0 or n_x>=4 or n_y>=4:
                    n_x -= dx[n_direc]
                    n_y -= dy[n_direc]
                    n_direc = (n_direc + 1) % 8
                    continue
                # 가는곳이 상어인경우
                if s_graph[n_x][n_y][2] == int(1e9):
                    n_x -= dx[n_direc]
                    n_y -= dy[n_direc]
                    n_direc = (n_direc + 1) % 8
                    continue
                temp = s_graph[n_x-dx[n_direc]][n_y-dy[n_direc]]
                s_graph[n_x-dx[n_direc]][n_y-dy[n_direc]] = s_graph[n_x][n_y]
                s_graph[n_x][n_y] = temp
                break
        return s_graph

    def dfs(graph,shark,total):
        s_graph = [g[:] for g in graph]
        sx,sy = shark
        total += s_graph[sx][sy][2]
        s_graph[sx][sy] = [0,0,int(1e9),s_graph[0][0][-1]]
        gra = fish_go(s_graph)
        s_graph = [g[:] for g in gra]
        shark_position = []
        sx, sy, s_num, s_direc = s_graph[shark[0]][shark[1]]
        for _ in range(4):
            sx += dx[s_direc]
            sy += dy[s_direc]
            if sx<0 or sy<0 or sx>=4 or sy>=4:
                continue
            if s_graph[sx][sy][2] != int(1e9):
                shark_position.append([s_graph[sx][sy][0],s_graph[sx][sy][1]])
        if len(shark_position) == 0:
            print(result,total)
            result[0] = max(result[0], total)
            return
        
        for nx,ny in shark_position:
            dfs(s_graph,[nx,ny],total)

    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,-1,-1,-1,0,1,1,1]
    graph = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        g = list(map(int,sys.stdin.readline().split()))
        for j,item in enumerate(g):
            if j % 2 == 0:
                graph[i][j//2] = [i,j//2,item]
            else:
                graph[i][j//2].append(item-1)

    shark = [0,0]
    result = [0]
    dfs(graph,shark,0)
    print(result[0])
if __name__ == '__main__':
    main()