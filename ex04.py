import sys

N,M,K = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    trees[a-1][b-1].append(c)

energy = [[5]*N for _ in range(N)]

dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]

for day in range(1,K+1):
    # 봄, 여름
    for i in range(N):
        for j in range(N):
            if len(trees[i][j]) <= 0:
                continue
            else:
                if day == 1:
                    trees[i][j].sort()
            k = 0
            while k < len(trees[i][j]):
                # 봄
                if trees[i][j][k] <= energy[i][j]:
                    energy[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                    k += 1
                else:
                    # 여름 (어차피 못먹고 죽음)
                    die = trees[i][j][k:]
                    for d in die:
                        energy[i][j] += d // 2
                    trees[i][j] = trees[i][j][:k]
                    break
    # 가을
    for i in range(N):
        for j in range(N):
            if len(trees[i][j]) == 0:
                continue
            for t in trees[i][j]:
                if t % 5 == 0:
                    for d in range(8):
                        nx = i + dx[d]
                        ny = j + dy[d]
                        if nx>=0 and ny>=0 and nx<N and ny<N:
                            trees[nx][ny].insert(0,1)

    # 겨울
    for i in range(N):
        for j in range(N):
            energy[i][j] += graph[i][j]
    
result = 0
for i in range(N):
    for j in range(N):
        result += len(trees[i][j])
print(result)












