from collections import deque
N = int(input())    # 보드의 크기
K = int(input())    # 사과의 개수 
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(K):
    a,b = map(int,input().split())
    graph[a][b] = 1 # 사과의 위치

L = int(input())
route1 = [list(map(str,input().split())) for _ in range(L)]
route = [[0,0] for _ in range(L)]
for i in range(len(route1)):
    if i==0:
        route[i][0] = int(route1[i][0])
    else:
        route[i][0] = int(route1[i][0])-int(route1[i-1][0])
    route[i][1] = route1[i][1]
route.append([int(1e9),0])

direction = [[0,1],[1,0],[0,-1],[-1,0]] # 동, 남, 서 , 북
now_direction = 0
cnt = 0
will_go =[0,0]

snake = deque()
head = [1,1]
snake.append(head)
flag = False

for r in route:
    for i in range(r[0]):
        will_go[0] = snake[-1][0] + direction[now_direction][0] # 다음에 이동할 머리 의 x 값
        will_go[1] = snake[-1][1] + direction[now_direction][1]
        if will_go in snake:    # 자기 자신에게 부딛치는 경우
            flag = True
            cnt+=1
            break
        if 1<=will_go[0]<=N and 1<=will_go[1]<=N:    # 테두리를 벗어나지 않을 시
            if graph[will_go[0]][will_go[1]] == 0:  # 먹이를 먹지 않을 시 
                snake.popleft()
                snake.append([will_go[0],will_go[1]])
                cnt+=1
            elif graph[will_go[0]][will_go[1]] == 1:    # 먹이를 먹을 시
                snake.append([will_go[0],will_go[1]])
                cnt+=1
                graph[will_go[0]][will_go[1]] = 0
        else: # 테두리를 벗어나는 경우
            flag = True
            cnt+=1
            break
        

    if flag:
        print(cnt)
        break

    if r[1]== "D":
        now_direction = (now_direction+1)%4
    elif r[1]== "L":
        now_direction = (now_direction-1)%4