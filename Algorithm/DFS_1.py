# 음료수 얼려먹기

# n x m 크기의 얼음 틀이있습니다 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은
# 1로 표시됩니다. 구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어있는 경ㅇ 서로 연결되어
# 있는 것으로 간주합니다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 
# 구하는 프로그램을 작성하세요.
# 4 5
# 00110
# 00011
# 11111
# 00000
# 답은 3

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False



# n,m을 공백을 기준으로 구분하여 입력 받기
n,m = map(int,input().split())

# 2차원 리스트의 맵 정보 입력 받기

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result +=1

# 정답 출력
print(result)

