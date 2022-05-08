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

'''
테스트 1 〉 통과 (343.33ms, 25.4MB)
테스트 2 〉 실패 (시간 초과)
테스트 3 〉 통과 (15.07ms, 25.3MB)
테스트 4 〉 실패 (시간 초과)
테스트 5 〉 통과 (14.65ms, 32.4MB)
테스트 6 〉 통과 (14.80ms, 32.2MB)
테스트 7 〉 실패 (시간 초과)
테스트 8 〉 통과 (15.27ms, 26.1MB)
테스트 9 〉 통과 (15.29ms, 26.2MB)

테스트 1 〉 통과 (333.19ms, 25.3MB)
테스트 2 〉 실패 (시간 초과)
테스트 3 〉 통과 (15.43ms, 25.1MB)
테스트 4 〉 실패 (시간 초과)
테스트 5 〉 통과 (15.52ms, 32.2MB)
테스트 6 〉 통과 (14.82ms, 32.3MB)
테스트 7 〉 실패 (시간 초과)
테스트 8 〉 통과 (15.36ms, 26.2MB)
테스트 9 〉 통과 (15.41ms, 26.1MB)

'''