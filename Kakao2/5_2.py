def solution(rc, operations):
    from collections import deque
    def Rotate(graph):
        number = graph[0][0]
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        n = len(graph)
        m = len(graph[0])
        nx,ny = [0,0]
        for d in range(4):
            while True:
                nx = nx + dx[d]
                ny = ny + dy[d]
                if nx>=0 and ny>=0 and nx<n and ny<m:
                    pass
                else:
                    nx = nx - dx[d]
                    ny = ny - dy[d]
                    break
                if nx ==0 and ny ==0 :
                    graph[nx-dx[d]][ny-dy[d]] = number
                    break
                graph[nx-dx[d]][ny-dy[d]] = graph[nx][ny]
        return graph

    def ShiftRow(graph):
        temp_g = graph.pop()
        graph.appendleft(temp_g)
        return graph

    q_graph = deque()
    for g in rc:
        q_graph.append(g)

    operation_edit = [[operations[0],1]]
    for i in range(1,len(operations)):
        if operations[i] == operation_edit[-1][0]:
            operation_edit[-1][1] += 1
        else:
            operation_edit.append([operations[i],1])

    for j in range(len(operation_edit)):
        if operation_edit[j][0] == "Rotate":
            operation_edit[j][1] %= (len(rc) + len(rc[0]))*2 - 4
        elif operation_edit[j][0] == "ShiftRow":
            operation_edit[j][1] %= len(rc)

    for oper in operation_edit:
        if oper[0] == "Rotate":
            for c1 in range(oper[1]):
                q_graph = Rotate(q_graph)
                q_graph = deque(q_graph)
        elif oper[0] == "ShiftRow":
            for c2 in range(oper[1]):
                q_graph = ShiftRow(q_graph)
                q_graph = deque(q_graph)

    ans = []
    for q in q_graph:
        ans.append(q)
        print(q)
    return ans

rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
operations = ["Rotate", "ShiftRow","Rotate","Rotate","Rotate","Rotate","Rotate","Rotate","Rotate","Rotate","ShiftRow","ShiftRow","ShiftRow"]

ans = solution(rc,operations)