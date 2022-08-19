import sys
from collections import deque


def newGame2():
    global position, mal, N, M
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for num in range(1, K+1, 1):
        x, y, direction = mal[num]
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 체스판을 벗어나지 않는 경우
        if nx >= 0 and ny >= 0 and nx < N and ny< N:
            # 흰색인 경우
            if color_graph[nx][ny] == 0:
                temp_queue = deque()
                for i in range(len(position[x][y])):
                    temp_num, temp_direction = position[x][y].popleft()
                    temp_queue.append([temp_num, temp_direction])
                    mal[temp_num] = [nx, ny, temp_direction]
                    if temp_num == num:
                        break
                for elem_num, elem_direc in position[nx][ny]:
                    temp_queue.append([elem_num, elem_direc])
                position[nx][ny] = temp_queue
                if len(position[nx][ny]) >= 4:
                    return True
                
            # 빨간색인 경우
            elif color_graph[nx][ny] == 1:
                for i in range(len(position[x][y])):
                    temp_num, temp_direction = position[x][y].popleft()
                    position[nx][ny].appendleft([temp_num, temp_direction])
                    mal[temp_num] = [nx, ny, temp_direction]
                    if len(position[nx][ny]) >= 4:
                        return True
                    if temp_num == num:
                        break
            # 파란색인 경우
            elif color_graph[nx][ny] == 2:
                nx = x - dx[direction]
                ny = y - dy[direction]
                # 방향 반대로 바꾸기
                if direction == 0:
                    direction = 1
                elif direction == 1:
                    direction = 0
                elif direction == 2:
                    direction = 3
                elif direction == 3:
                    direction = 2
                if nx >= 0 and ny >= 0 and nx < N and ny < N:
                    # 방향 바꿨는데 흰색인 경우
                    if color_graph[nx][ny] == 0:
                        temp_queue = deque()
                        for i in range(len(position[x][y])):
                            temp_num, temp_direction = position[x][y].popleft()
                            temp_queue.append([temp_num, temp_direction])
                            mal[temp_num] = [nx, ny, temp_direction]
                            # print("hi",direction,[nx,ny],num)
                            if temp_num == num:
                                temp_queue[-1][1] = direction
                                mal[num] = [nx, ny, direction]
                                break
                        for elem_num, elem_direc in position[nx][ny]:
                            temp_queue.append([elem_num, elem_direc])
                        position[nx][ny] = temp_queue
                        if len(position[nx][ny]) >= 4:
                            return True
                    # 방향 바꿨는데 빨간색인 경우
                    elif color_graph[nx][ny] == 1:
                        for i in range(len(position[x][y])):
                            temp_num, temp_direction = position[x][y].popleft()
                            position[nx][ny].appendleft([temp_num, temp_direction])
                            mal[temp_num] = [nx, ny, temp_direction]
                            if len(position[nx][ny]) >= 4:
                                return True
                            if temp_num == num:
                                position[nx][ny][0][1] = direction
                                mal[num] = [nx, ny, direction]
                                break
                    # 방향 바꿨는데 파란색인 경우 => 이동 X
                    elif color_graph[nx][ny] == 2:
                        mal[num][2] = direction
                        for j in range(len(position[x][y])):
                            if position[x][y][j][0] == num:
                                position[x][y][j][1] = direction
                                break
                # 방향 바꿨는데 외부로 벗어나는 경우 => 이동 X
                else:
                    mal[num][2] = direction
                    for j in range(len(position[x][y])):
                        if position[x][y][j][0] == num:
                            position[x][y][j][1] = direction
                            break
                
        # 체스판을 벗어나는 경우 => 파란색 => 방향 전환
        else:
            nx = x - dx[direction]
            ny = y - dy[direction]
            # 방향 반대로 바꾸기
            if direction == 0:
                direction = 1
            elif direction == 1:
                direction = 0
            elif direction == 2:
                direction = 3
            elif direction == 3:
                direction = 2
            # 벽만나서 방향 바꿨는데 흰색인 경우
            if color_graph[nx][ny] == 0:
                temp_queue = deque()
                for i in range(len(position[x][y])):
                    temp_num, temp_direction = position[x][y].popleft()
                    temp_queue.append([temp_num, temp_direction])
                    mal[temp_num] = [nx, ny, temp_direction]
                    if temp_num == num:
                        temp_queue[-1][1] = direction
                        mal[num] = [nx, ny, direction]
                        break
                for elem_num, elem_direc in position[nx][ny]:
                    temp_queue.append([elem_num, elem_direc])
                position[nx][ny] = temp_queue
                if len(position[nx][ny]) >= 4:
                    return True
            # 벽만나서 방향 바꿨는데 빨간색인 경우
            elif color_graph[nx][ny] == 1:
                for i in range(len(position[x][y])):
                    temp_num, temp_direction = position[x][y].popleft()
                    position[nx][ny].appendleft([temp_num, temp_direction])
                    mal[temp_num] = [nx, ny, temp_direction]
                    if len(position[nx][ny]) >= 4:
                        return True
                    if temp_num == num:
                        position[nx][ny][0][1] = direction
                        mal[num] = [nx, ny, direction]
                        break
            # 벽만나서 방향 바꿨는데 파란색인 경우
            elif color_graph[nx][ny] == 2:
                mal[num][2] = direction
                for j in range(len(position[x][y])):
                    if position[x][y][j][0] == num:
                        position[x][y][j][1] = direction
                        break
                

        # print(num)
        # print(mal)
        # for p in position:
        #     # print(p)
        #     for t in p:
        #         print(len(t), end = " ")
        #     print()
        # for p in position:
        #     print(p)
        # print()

    return False



N, K = map(int,input().split())

color_graph = [list(map(int,input().split())) for _ in range(N)]
position = [[deque() for _ in range(N)] for _ in range(N)]
mal = {}
for num in range(1, K + 1, 1):
    x, y, direc = map(int,input().split())
    mal[num] = [x - 1, y - 1, direc - 1]
    position[x-1][y-1].append([num, direc-1])
# for p in position:
#     print(p)
# print()
count = 0
while 1:
    count += 1
    result_flag = newGame2()
    if result_flag:
        # for p in position:
        #     # print(p)
        #     for t in p:
        #         print(len(t), end = " ")
        #     print()
        print(count)
        break
    if count == 1000:
        # for p in position:
        #     print(p)
        print(-1)
        break
    # break
    # for p in position:
    #     print(p)
    # print("*"*10)
    # print(mal)

