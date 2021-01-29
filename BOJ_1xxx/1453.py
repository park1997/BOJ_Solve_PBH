# 피시방 알바
a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in b:
    if i in c:
        d.append(i)
    else: 
        c.append(i)
print(len(d))