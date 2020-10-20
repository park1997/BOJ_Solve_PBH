a,b,c = map(int,input().split())
total_c =0
if b<c:
    print((a//(c-b))+1)
elif b>=c:
    print(-1)
