'''
nxm 크기의 금광이 있습니다. 금광은 1x1 크기의 칸으로 나누어져 있으며, 
각 칸은 특정한 크기의 금이 들어있습니다.
채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 
맨 처음에는 첫 번째 열의 어느 행에서든 출발 할 수 있습니다. 이후에 m-1번에 걸쳐서 매번
오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.

첫째줄에 테스트 케이스 T가 입력됩니다
매 테스트 케이스 첫째 줄에 n,m이 공백으로 구분되어 입력됩니다
둘째 줄에 nxm개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다

입력예시 
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4 
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2 

출력예시 
19
16
'''

T = int(input())
for i in range(T):
    n,m = map(int,input().split())
    data = list(map(int,input().split()))
    
    dp =[]
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(data[i*m+j])
        dp.append(temp)
    
    for j in range(1,m):
        if i==n-1:
            max_num = dp[i][j]
        for i in range(n):
            if i==0:
                dp[i][j] = max(dp[i][j-1],dp[i+1][j-1])+dp[i][j]
            elif i==n-1:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j-1])+dp[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i][j-1],dp[i+1][j-1])+dp[i][j]
            if dp[i][j] > max_num:
                max_num = dp[i][j]
    print(max_num)