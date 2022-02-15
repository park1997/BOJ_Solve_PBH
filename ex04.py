import sys
N,M = map(int,sys.stdin.readline().split())
ice = list(map(int,input().split()))
ice.sort()

x = 1
y = ice[-1]
ans = 0
while x<=y:
    mid = (x+y)//2
    cnt = 0
    for i in range(len(ice)):
        if ice[i] >= mid:
            cnt += ice[i]//mid
    if cnt >= N:
        x = mid + 1
        ans = mid
    else:
        y = mid - 1
print(ans)
    