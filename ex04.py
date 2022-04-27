import sys
import heapq
def main():
    

    R,C,M = map(int,sys.stdin.readline().split())
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    graph = [[""]*C for _ in range(R)]
    shark = []
    for m in range(M):
        r,c,s,d,z = map(int,sys.stdin.readline().split())
        shark.append([r-1,c-1,s,d-1,z])
        graph[r-1][c-1] = [r-1 , c-1 , s , d-1 , z]
    gain = 0
    def hunt(king):
        global dx,dy,R,C,graph
        for i in range(R):
            for j in range(C):
                if j == king and len(graph[i][j])!=0:
                    a = graph[i][j][-1]
                    graph[i][j] = ""
                    return a
        return 0 
    def move():
        global dx,dy,R,C,graph
        q = []
        for i in range(R):
            for j in range(C):
                if len(graph[i][j]) != 0:
                    r,c,s,d,z = graph[i][j]
                    heapq.heappush(q,[z,r,c,s,d])
        new_graph = [[""]*C for _ in range(R)]
        while q:
            z1,r1,c1,s1,d1 = heapq.heappop(q)
            if s1 == 0:
                new_graph[r1][c1] = [r1 ,c1 ,s1 ,d1 ,z1]
                continue
            cnt = 0
            distance = s1 % (2 * C)
            while 1:
                cnt += 1
                r1 += dx[d1]
                c1 += dy[d1]
                if r1<0 or c1<0 or r1>=R or c1>=C:
                    r1 -= 2 * dx[d1]
                    c1 -= 2 * dy[d1]
                    # 방향 전환
                    if d1 == 0:
                        d1 = 1
                    elif d1 == 1:
                        d1 = 0
                    elif d1 == 2:
                        d1 = 3
                    elif d1 == 3:
                        d1 = 2
                if cnt == distance:
                    cnt = 0
                    break
            new_graph[r1][c1] = [r1 ,c1 ,s1 ,d1 ,z1]
        return new_graph
    for king in range(C):
        g = hunt(king)
        gain += g
        n_g = move()
        graph = [ng[:] for ng in n_g]
    print(gain)

if __name__=="__main__":
    main()