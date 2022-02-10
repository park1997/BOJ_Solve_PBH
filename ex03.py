import copy
from itertools import combinations
from collections import deque
N = int(input())
s_to_e = [[i,j] for i in range(N) for j in range(N)]
arr = [list(map(str,input().split())) for _ in range(N)]
result = -1
combi = list(combinations(s_to_e,2))
for c in combi:
    s_x,s_y = c[0][0],c[0][1]
    target_x,target_y = c[1][0], c[1][1]

    d = deque()
    ans = [[0]*N for i in range(N)]

    visited_wall = [[0]*N for i in range(N)]

    visited_wall[s_x][s_y]=1

    d.append((s_x,s_y,0,True,visited_wall,ans)) #i,j,cnt,wall,visted_wall

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    M = 0
    while d:
        i,j,cnt,flag,wall,Answer = d.popleft()
        if Answer[target_x][target_y]:
            M = max(M,Answer[target_x][target_y])
        for k in range(4):
            i2 = i+dx[k]
            j2 = j+dy[k]
            if (0<=i2<N and 0<=j2<N) and wall[i2][j2]==0:
                if ord(arr[i][j])<ord(arr[i2][j2]):
                    copy_wall = copy.deepcopy(wall)
                    answer = copy.deepcopy(Answer)
                    answer[i2][j2]=Answer[i][j]+1
                    copy_wall[i2][j2]=1
                    d.append((i2,j2,cnt+1,flag,copy_wall,answer))
                elif ord(arr[i][j])>=ord(arr[i2][j2]) and flag:
                    if Answer[i][j]<cnt+1 and wall[i2][j2]==0:
                        copy_wall = copy.deepcopy(wall)
                        answer = copy.deepcopy(Answer)
                        answer[i2][j2]=Answer[i][j]+1
                        copy_wall[i2][j2]=1
                        d.append((i2,j2,cnt+1,False,copy_wall,answer))
        for w in wall:
            print(w)
        print()
    if M+1 > result:
        result = M+1
print(result)


'''
5
A B C F F
F F D E F
F F F F F
C B A G H
D E F G H

4
A B C D
G F E D
H I J K
O N M L

3
2 2
A B C
E D C
F G H
'''