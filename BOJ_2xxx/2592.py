# 대표값
a=[int(input()) for i in range(10)]
b=[]
print(sum(a)//10)
c=list(set(a))
for i in c:
    b.append(a.count(i))
print(c[b.index(max(b))])
