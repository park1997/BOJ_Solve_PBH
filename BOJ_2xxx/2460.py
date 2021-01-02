# 지능형기차 2
c=0
d=[]
for i in range(10):
    a,b=map(int,input().split())
    c=c-a
    c=c+b
    d.append(c)
print(max(d))
