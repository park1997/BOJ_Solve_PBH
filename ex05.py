n = int(input())
graph = [list(input()) for _ in range(n)]

row = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if graph[i][j] == ".":
            cnt +=1
        else:
            if cnt >= 2:
                row +=1
                cnt = 0
            else:
                cnt = 0
    if cnt>=2:
        row +=1

col = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if graph[j][i] ==".":
            cnt +=1
        else:
            if cnt >=2:
                col +=1
                cnt = 0
            else:
                cnt = 0
    if cnt >=2:
        col +=1

print(row,col)