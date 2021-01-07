# 나는 요리사다
a=[list(map(int,input().split())) for i in range(5)]
b=[]
for i in a:
    b.append(sum(i))
print(b.index(max(b))+1)
print(max(b))
