'''
4 6
19 15 10 17
'''
N,M = map(int,input().split())
rc = list(map(int,input().split()))
start = 0
end = max(rc)
def slice(rc,mid):
    result = 0
    for i in rc:
        if i>mid:
            result += (i-mid)
    return result
while start <= end:
    mid = (start+end)//2
    if slice(rc,mid) > M:
        start = mid +1
    elif slice(rc,mid) < M:
        end = mid -1
    else:
        break
print(mid)
