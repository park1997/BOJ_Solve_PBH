# 홀수
a=[int(input()) for i in range(7)]
b=[i for i in a if i%2==1]
if sum(b)==0:
    print(-1)
else:
    print(sum(b))
    b.sort()
    print(b[0])
