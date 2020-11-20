#R2
a,b=map(int,input().split())
if a<b:
    print(b+(b-a))
else:
    print(b-(a-b))
