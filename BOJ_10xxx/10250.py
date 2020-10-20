a=int(input())

for i in range(a):
    h,w,n=map(int,input().split())
    x = n%h
    y = n//h
    if x!=0:
        print((x*100)+y+1)
    elif x == 0:
        x= h
        print((x*100)+y)
