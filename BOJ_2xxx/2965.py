# 캥거루 세마리
a=list(map(int,input().split()))
count=0
while len(set(a))==3:
    if a[1]-a[0]<=a[2]-a[1]:
        a[0]=a[2]-1
        a.sort()
        count+=1
    else:
        a[2]=a[0]+1
        a.sort()
        count+=1
print(count-1)