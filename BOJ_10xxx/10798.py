# 세로읽기
a=[input() for i in range(5)]
j=0
length=[len(i) for i in a]
x=max(length)
new_a=[]
for i in a:
    if len(i)==x:
        new_a.append(i)
        pass
    else:
        new_a.append(i+" "*(x-len(i)))
k=0
result=[]
while k<x:
    for i in new_a:
        result.append(i[k])
    k+=1
result="".join(result).split()
print(*result,sep="")