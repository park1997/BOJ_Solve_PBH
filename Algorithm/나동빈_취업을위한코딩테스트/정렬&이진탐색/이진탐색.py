a,target = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
start = 0
end = len(l)
flag = False
while start <= end:
    mid = (start+end)//2
    if l[mid] < target:
        start = mid + 1
    elif l[mid] > target:
        end = mid -1
    else:
        flag = True
        break

if flag:
    print(mid)
else:
    print("찾을 수 없습니다.")


