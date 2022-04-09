import sys
N = int(sys.stdin.readline())
student = {}
for _ in range(N**2):
    a = list(map(int,sys.stdin.readline().split()))
    student[a[0]] = a[1:]
s_class = [[0]*N for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for s in student:
    empty_count = {}
    for i in range(N):
        for j in range(N):
            if s_class[i][j] != 0:
                continue
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if nx>=0 and ny>=0 and nx<N and ny<N:
                    target = str(i)+" "+str(j)
                    if target in empty_count:
                        if s_class[nx][ny] == 0:
                            empty_count[target][0] += 1
                        if s_class[nx][ny] in student[s]:
                            empty_count[target][1] += 1
                    else:
                        if s_class[nx][ny] == 0:
                            empty_count[target] = [1,0]
                        else:
                            empty_count[target] = [0,0]
                        if s_class[nx][ny] in student[s]:
                            empty_count[target][1] += 1
    max_ne = -1
    max_love = -1
    posi = [-1,-1]
    for e in empty_count:
        if empty_count[e][1] >= max_love:
            if posi == [-1,-1]:
                posi = e.split()
                max_love = empty_count[e][1]
                max_ne = empty_count[e][0]
                continue
            if empty_count[e][1] > max_love:
                posi = e.split()
                max_love = empty_count[e][1]
                max_ne = empty_count[e][0]
                continue
            if empty_count[e][0] > max_ne:
                posi = e.split()
                max_ne = empty_count[e][0]
                max_love = empty_count[e][1]
    s_class[int(posi[0])][int(posi[1])] = s

result = 0
for i1 in range(N):
    for j1 in range(N):
        temp_result = 0
        for d1 in range(4):
            nx1 = i1 + dx[d1]
            ny1 = j1 + dy[d1]
            if nx1>=0 and ny1>=0 and nx1<N and ny1<N:
                if s_class[nx1][ny1] in student[s_class[i1][j1]]:
                    temp_result += 1
        if temp_result == 0:
            result += 0
        elif temp_result == 1:
            result += 1
        elif temp_result == 2:
            result += 10
        elif temp_result == 3:
            result += 100
        elif temp_result == 4:
            result += 1000
print(result)