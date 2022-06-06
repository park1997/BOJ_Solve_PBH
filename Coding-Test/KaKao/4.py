def solution(n, start, end, roads, traps):
    roads = roads
    traps = traps
    result =0
    start = start
    while 1:
        for i in range(len(roads)):
            if roads[i][0]==start:
                result+=roads[i][2]
                start = roads[i][1]
                for j in range(len(roads)):
                    if (roads[j][1] or roads[j][0]) in traps:
                        temp = roads[j][0]
                        roads[j][0]=roads[j][1]
                        roads[j][1]= temp
        if start == end:
            break
    return result
print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]],[2]))
