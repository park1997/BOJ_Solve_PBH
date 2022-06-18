from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def rotate_and_melting(board, len_board, L):
    """
    Level에 맞게 회전 후 얼음을 녹임
    :param board: 보드
    :param len_board: 보드 길이
    :param L: level
    :return:
    """
    new_board = [[0] * len_board for _ in range(len_board)] # 회전한 Board 저장 용

    # rotate
    r_size = 2 ** L # 격자 사이즈
    for y in range(0, len_board, r_size): # 격자 시작 좌표 y축
        for x in range(0, len_board, r_size): # 격자 시작 좌표 x축
            for i in range(r_size): # 열 인덱스
                for j in range(r_size): # 행 인덱스
                    new_board[y + j][x + r_size - i - 1] = board[y + i][x + j]

    board = new_board
    melting_list = [] # 녹을 얼음 좌표
    for y in range(len_board):
        for x in range(len_board):
            ice_count = 0
            for d in range(len(dy)):
                ny = y + dy[d]
                nx = x + dx[d]

                if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board:
                    continue
                elif board[ny][nx] > 0:
                    ice_count += 1

            if ice_count < 3 and board[y][x] != 0:
                melting_list.append((y, x))
    print(melting_list)
    for b in board:
        print(b)
    print()

    # 저장된 얼음들을 녹임
    for y, x in melting_list:
        board[y][x] -= 1
    for b in board:
        print(b)
    print()
    return board

def check_ice_bfs(board, len_board):
    """
    얼음 상태 확인
    :param board: 보드
    :param len_board: 보드 가로 길이
    :return:
    """
    used = [[False] * len_board for _ in range(len_board)]
    ice_sum = 0
    max_area_count = 0
    for y in range(len_board):
        for x in range(len_board):
            area_count = 0
            if used[y][x] or board[y][x] == 0:
                continue
            # BFS를 이용하여 얼음 덩어리 조사
            q = deque()
            q.append((y, x))
            used[y][x] = True

            while q:
                sy, sx = q.popleft()
                ice_sum += board[sy][sx] # 얼음 합 추가
                area_count += 1  # 얼음 카운트 추가

                for d in range(4):
                    ny = sy + dy[d]
                    nx = sx + dx[d]
                    if nx < 0 or ny < 0 or nx >= len_board or ny >= len_board or used[ny][nx]:
                        continue
                    if board[ny][nx] != 0:
                        used[ny][nx] = True
                        q.append((ny, nx))

            max_area_count = max(max_area_count, area_count) # 최대 얼음 덩어리 크기 파악

    print(ice_sum)
    print(max_area_count)


def solve():
    N, Q = map(int, input().split(' '))
    len_board = 2 ** N
    board = [list(map(int, input().split(' '))) for _ in range(len_board)]
    L_list = list(map(int, input().split(' ')))

    for L in L_list:
        board = rotate_and_melting(board, len_board, L)

    check_ice_bfs(board, len_board)

solve()