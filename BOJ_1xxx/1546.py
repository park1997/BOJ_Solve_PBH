a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(a):
    c.append((b[i]/max(b))*100)

average=sum(c)/a
print(average)
