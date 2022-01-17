import sys
a=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))
result=[]
num=[]
for i in range(a):
    x=0
    y=len(result)-1
    while x<=y:
        mid=(x+y)//2
        if result[mid]<b[i]:
            x=mid+1
        else:
            y=mid-1
    if x>=len(result):
        result.append(b[i])
        num.append(x)
    else:
        result[x]=b[i]
        num.append(x)
print(len(result))
c=max(num)
nom=[]
for i in range(num.index(c),-1,-1):
    if num[i]==c:
        nom.append(b[i])
        c-=1
print(*reversed(nom))
