# 감시피하기
import sys
from itertools import combinations
from collections import deque
N = int(sys.stdin.readline())
graph = []
teacher = []
for i in range(N):
    graph.append(list(map(str,sys.stdin.readline().split())))
    for j in range(N):
        if graph[i][j] == "T":
            teacher.append([i,j])
obstacles = list(combinations(list(range(N**2)),3))
def bfs(o_list):
    global q
    while q:
        tx,ty = q.popleft()
        for i in range(4):
            for j in range(1,N):
                t_tx = tx+dx[i]*j
                t_ty = ty+dy[i]*j
                if t_tx>=0 and t_ty>=0 and t_tx<N and t_ty<N:
                    if graph[t_tx][t_ty]=="S":
                        return False
                    if (t_tx,t_ty) in o_list:
                        break
                else:
                    break
    return True


dx = [0,1,0,-1]
dy = [1,0,-1,0]
for o in obstacles:
    flag = False
    o1,o2,o3 = o
    o1 = (o1//N,o1%N)
    o2 = (o2//N,o2%N)
    o3 = (o3//N,o3%N)
    o_list = [(o1[0],o1[1]),(o2[0],o2[1]),(o3[0],o3[1])]
    q = deque(teacher)
    if graph[o1[0]][o1[1]] == "X" and graph[o2[0]][o2[1]] == "X" and graph[o3[0]][o3[1]] == "X":
        if bfs(o_list):
            flag = True
            print("YES")
            break

if not flag:
    print("NO")

