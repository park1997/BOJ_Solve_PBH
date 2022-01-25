N = int(input())
num = list(map(int,input().split()))
M = int(input())
start = 0
end = 0
result = num[start]
cnt = 0
while start<=end:
    try:
        if result<=M:
            end+=1
            result += num[end]
        elif result>M:
            result-=num[start]
            start+=1
            cnt += N-end
    except:
        break
print(cnt)

