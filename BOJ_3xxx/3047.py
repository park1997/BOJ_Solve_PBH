# ABC
a=list(map(int,input().split()))
a.sort()
b=input()
tmp=[]
for i in b:
    if i=='A':
        tmp.append(a[0])
    elif i=='B':
        tmp.append(a[1])
    elif i=='C':
        tmp.append(a[2])
print(*tmp)