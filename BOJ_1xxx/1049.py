a,b=map(int,input().split())
set_6=[]
num=[]
new=[]
for i in range(b):
    s,n=map(int,input().split())
    set_6.append(s)
    num.append(n)
for i in range(b):
    new.append(a*num[i])
    if a<=6:
        new.append(set_6[i])
    else:
        new.append(((a//6)+1)*min(set_6))
        new.append((a//6)*min(set_6)+min(num)*(a-((a//6)*6)))
print(min(new))
