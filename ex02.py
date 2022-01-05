N = int(input())
data = [list(map(int,input().split())) for i in range(N)]
data.sort(key=lambda x: (x[1],x[0]))    # 가장 먼저 끝나느 회의 순으로 회의를 정렬
result = 1
s = data[0][0]  # start 포인트, 회의의 시작시간
e = data[0][1]  # end 포인트, 회의의 끝나는 시간
for i in range(1,len(data)):    # 가장 먼저 끝나느 회의중 첫번째 회의는 무조건 진행하므로 for loop는  1부터 탐색 시작
    if data[i][0]>=e: # 만약에 현재 회의의 끝나는 시간보다 크거나 같은 시작시간을 가지고있는 회의를 발견할 시 그 회의 선택 
        s = data[i][0]  # 회의의 start시간 update
        e = data[i][1]  # 회의의 end시간 update
        result+=1   # 결과 +=1
print(result)
