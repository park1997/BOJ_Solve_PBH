a,b,c =map(int,input().split())
count = 0
while a>=0 and b>=0 and a+b>=c:
    a-=2
    b-=1
    count+=1
print(count-1)
