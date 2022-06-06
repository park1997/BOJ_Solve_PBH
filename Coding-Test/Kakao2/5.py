def solution(rc, operations):
    def shiftrow(graph):
        graph.insert(0,graph.pop())
        return graph
    def rotate(graph,N,M):
        start_num = graph[0][0]
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        nx,ny = [0,0]
        for i in range(4):
            while 1:
                nx += dx[i]
                ny += dy[i]
                if nx<0 or ny<0 or nx>=N or ny>=M:
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                if [nx,ny] == [0,0]:
                    graph[nx-dx[i]][ny-dy[i]] = start_num
                    break
                graph[nx-dx[i]][ny-dy[i]] = graph[nx][ny]
        return graph
    
    N = len(rc)
    M = len(rc[0])
    new_operation = [[operations[0],1]]
    n = len(operations)
    for i in range(1,n):
        target,cnt = new_operation[-1]
        if operations[i] == target:
            new_operation[-1][1] += 1
        else:
            new_operation.append([operations[i],1])
    
    for i in range(len(new_operation)):
        order,count = new_operation[i]
        if order == "Rotate":
            new_operation[i][1] %= N*2 + M*2 - 4
        else:
            new_operation[i][1] %= N
    print(new_operation)
    for oper in new_operation:
        op,cnt = oper
        if cnt == 0:
            continue
        if op == "Rotate":
            for _ in range(cnt):
                rc = rotate(rc,N,M)
        else:
            for _ in range(cnt):
                rc = shiftrow(rc)
    for r in rc:
        print(r)
    return rc


rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
operations = ["Rotate", "ShiftRow","Rotate","Rotate","Rotate","ShiftRow","ShiftRow","ShiftRow","ShiftRow","ShiftRow","ShiftRow","ShiftRow","ShiftRow"]

ans = solution(rc,operations)

# 상수시간 안에 쉬프트 돌리고 싶다
