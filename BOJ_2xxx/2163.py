#초콜릿 자르기
a=list(map(int,input().split()))
a.sort()
print((a[0]-1)+(a[1]-1)*a[0])
