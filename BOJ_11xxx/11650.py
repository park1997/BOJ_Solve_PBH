n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
a.sort()
for i in a:
    print("{} {}".format(i[0],i[1]))
