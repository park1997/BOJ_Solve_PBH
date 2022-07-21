import sys
N, M, k = map(int, sys.stdin.readline().split())
graph = [[0] * N for _ in range(N)]
shark_posi = {}

for i in range(N):
    gra = list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        if gra[j] != 0:
            shark_posi[gra[j]] = [i,j]



# 위 아래 왼 오 = (1,2,3,4)
shark_first_direc = {0 : 0}
sfd = list(map,int, sys.stdin.readline().split())
for idx, s in enumerate(sfd):
    shark_first_direc[idx] = s


shark_direc = {}

for i in range(1, M + 1, 1):
    d = list(map(int,sys.stdin.readline().split()))
    for j, ele in enumerate(d:)

