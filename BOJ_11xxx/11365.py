# 1밀비 급일
while 1:
    a=list(map(str,input().split()))
    if a[0]=='END':
        break
    for i in range(len(a)):
        a[i]=a[i][::-1]
    print(*a[::-1])