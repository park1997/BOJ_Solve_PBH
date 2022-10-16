import sys
from collections import deque
def game(player):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for pp in range(1, len(player) + 1, 1):
        x, y, direc, s, gs = player[pp]
        new_direc = direc
        for d in range(2):
            nx = x + dx[new_direc]
            ny = y + dy[new_direc]
            print(nx,ny)
            # 그래프 안에 있다면.
            if 0 <= nx < N and 0 <= ny < N:
                gun_graph[nx][ny].sort()
                max_gun_stat = gun_graph[nx][ny][-1]
                my_max_gun_stat = max(gs)
                # 이동한 방향에 총이 있는 경우
                if my_max_gun_stat < max_gun_stat:
                    elem = gun_graph[nx][ny].pop()
                    gs.appendleft(elem)
                    for _ in range(len(gs) - 1):
                        gun_graph[nx][ny].append(gs.pop())
                # 총이 없는 경우
                else:
                    pass
                print(nx, ny, new_direc,"gdg111")
                # 이동한 방향에 플레이어가 있는 경우
                if player_graph[nx][ny][0] != 0:
                    fight_player_num, fight_player_s, fight_player_g = player_graph[nx][ny]
                    my_s, my_g = s, max(gs)
                    # 내가 능력치가 더 높은 경우
                    if my_s + my_g > fight_player_s + fight_player_g:
                        result[pp] += 1
                        # 내가 가진총 내려놓기
                        while gs:
                            gun_graph.append(gs.pop())
                        # 게임에서 지고 갈수있는 방향 찾기
                        for dd in range(4):
                            new_direc = (new_direc + dd) % 4
                            new_nx = nx + dx[new_direc]
                            new_ny = ny + dy[new_direc]
                            print(new_nx, new_ny, "really")
                            # 그래프 안에있으면서 플레이어가 없는 곳이라면
                            if 0 <= new_nx < N and 0 <= new_ny < N and player_graph[new_nx][new_ny][0] != 0:
                                gun_graph[new_nx][new_ny].sort()
                                max_gun_stat = gun_graph[new_nx][new_ny][-1]
                                my_max_gun_stat = my_g
                                # 이동한 방향에 총이 있는 경우
                                if my_max_gun_stat < max_gun_stat:
                                    elem = gun_graph[nx][ny].pop()
                                    gs.appendleft(elem)
                                    for _ in range(len(gs) - 1):
                                        gun_graph[nx][ny].append(gs.pop())
                                # 간곳에 총이 없는 경우
                                else:
                                    pass
                                player_graph[new_nx][new_ny] = [pp, my_s, my_g]
                                player[pp] = [new_nx, new_ny, new_direc, my_s, gs]
                                player_graph[x][y] = [0, 0, 0]
                                break
                            else:
                                continue
                        # 승리자는 패배자가 떨어트린 총을 가져가기
                        
                    
                    # 내 능력치가 더 낮은 경우
                    else:
                        result[fight_player_num] += 1
                        # 내가 가진총 내려놓기
                        while gs:
                            gun_graph.append(gs.pop())
                        # 게임에서 지고 갈수있는 방향 찾기
                        for dd in range(4):
                            new_direc = (new_direc + dd) % 4
                            new_nx = nx + dx[new_direc]
                            new_ny = ny + dy[new_direc]
                            print(new_nx, new_ny, "realluuu")
                            # 그래프 안에있으면서 플레이어가 없는 곳이라면
                            if 0 <= new_nx < N and 0 <= new_ny < N and player_graph[new_nx][new_ny][0] == 0:
                                gun_graph[new_nx][new_ny].sort()
                                max_gun_stat = gun_graph[new_nx][new_ny][-1]
                                my_max_gun_stat = my_g
                                # 이동한 방향에 총이 있는 경우
                                if my_max_gun_stat < max_gun_stat:
                                    elem = gun_graph[nx][ny].pop()
                                    gs.appendleft(elem)
                                    for _ in range(len(gs) - 1):
                                        gun_graph[nx][ny].append(gs.pop())
                                # 간곳에 총이 없는 경우
                                else:
                                    pass
                                player_graph[new_nx][new_ny] = [pp, my_s, my_g]
                                player[pp] = [new_nx, new_ny, new_direc, my_s, gs]
                                player_graph[x][y] = [0, 0, 0]
                                print(new_nx, new_ny, "asd")
                                break
                            else:
                                continue

                # 이동한 방향에 플레이어가 없는 경우
                elif player_graph[nx][ny][0] == 0:
                    player[pp] = [nx, ny, new_direc, s, gs]
                    player_graph[x][y] = [0, 0, 0]
                    player_graph[nx][ny] = [pp, s, max(gs)]
                for pp in player_graph:
                    print(pp)
                print()

                break
            # 그래프 안에 없다면
            else:
                new_direc = (direc + 2) % 4



N, M, K = map(int, sys.stdin.readline().split())
gun_graph = [[[] for _ in range(N)] for _ in range(N)]

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        gun_graph[i][j].append(temp[j])

player_graph = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

player = {}
for p in range(1, M + 1, 1):
    x, y, d, s = map(int, sys.stdin.readline().split())
    player[p] = [x - 1, y - 1, d, s, deque([0])]
    player_graph[x - 1][y - 1][0] = p
    player_graph[x - 1][y - 1][1] = s

for pp in player_graph:
    print(pp)
print()

result = [0] *(M + 1)
for k in range(K):
    game(player)
    print(result)
