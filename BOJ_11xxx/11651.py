import sys
n=int(sys.stdin.readline())
a=[list(map(int,sys.stdin.readline().split()))[::-1] for i in range(n)]
a.sort()
for i in a:
    print("{} {}".format(i[1],i[0]))
