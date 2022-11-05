def solution(rows, columns, swipes):
    result = []
    graph = []
    for i in range(1,rows + 1, 1):
        t = [(i-1) * columns + j for j in range(1, columns + 1, 1)]
        graph.append(t)
    for s in swipes:
        d, r1, c1, r2, c2 = s[0], s[1] - 1, s[2] - 1, s[3] - 1, s[4] - 1
        part_ans = 0
        part = []
        if d == 1:
            for i in range(r1, r2 + 1, 1):
                temp = []
                for j in range(c1, c2 + 1, 1):
                    temp.append(graph[i][j])
                    if i == r2:
                        part_ans += graph[i][j]
                if i == r2:
                    part.insert(0, temp)
                else:
                    part.append(temp)
        elif d == 2:
            for i in range(r1, r2 + 1, 1):
                temp = []
                for j in range(c1, c2 + 1, 1):
                    temp.append(graph[i][j])
                    if i == r1:
                        part_ans += graph[i][j]
                    part.append(temp)
            part.append(part[0])
            del part[0]
        elif d == 3:
            for i in range(r1, r2 + 1, 1):
                temp = []
                for j in range(c1, c2 + 1, 1):
                    temp.append(graph[i][j])
                    if j == c2:
                        part_ans += graph[i][j]
                        temp.insert(0, graph[i][j])
                        del temp[-1]
                part.append(temp)
        elif d == 4:
            for i in range(r1, r2 + 1, 1):
                temp = []
                for j in range(c1, c2 + 1, 1):
                    temp.append(graph[i][j])
                    if j == c1:
                        part_ans += graph[i][j]
                temp.append(temp[0])
                del temp[0]
                part.append(temp)
        x, y = 0, 0
        for i in range(r1, r2 + 1, 1):
            for j in range(c1, c2 + 1, 1):
                graph[i][j] = part[x][y]
                y += 1
            x += 1
            y = 0
        result.append(part_ans)
    return result


rows = 4
columns = 3
swipes =[[1,1,2,4,3],[3,2,1,2,3],[4,1,1,4,3],[2,2,1,3,3]]
r = solution(rows, columns, swipes)
print(r)





6 시그마 
과제 정의 단계 
-> voc -> ccr -> CTQ 도출 과정이 가지는 의미 의미
CTQ 가 무었인지 확실히 알기 