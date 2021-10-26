width, height = 10, 10
row, col, color = 5, 5, 1
map_ = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
queue = []


def bfs(coord, color):
    global map_, queue
    queue.append(coord)
    map_[coord[0]][coord[1]] = color
    while len(queue) != 0:
        front = queue.pop(0)
        for (drow, dcol) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if (0 <= front[0]+drow < height and 0 <= front[1]+dcol < width) and map_[front[0]+drow][front[1]+dcol] == 0:
                queue.append((front[0]+drow, front[1]+dcol))
                map_[front[0]+drow][front[1]+dcol] = color

bfs((row, col), color)
for i in range(height):
    for j in range(width):
        print(map_[i][j], end='')
    print('')