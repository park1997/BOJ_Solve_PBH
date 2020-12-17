# 최댓값
a=[list(map(int,input().split())) for i in range(9)]
b=[max(i) for i in a]
print(max(b))
print("{} {}".format(b.index(max(b))+1,a[b.index(max(b))].index(max(b))+1))
