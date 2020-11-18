a=int(input())
b=[]
for i in range(a):
    b.append(list(map(str,input().split())))
b=sorted(b,key=lambda x:(-int(x[1]),x[0]))
print(b[0][0])
