import sys
a=int(sys.stdin.readline())
b=[list(map(str,sys.stdin.readline().split())) for i in range(a)]
b.sort(key=lambda x:int(x[0]))
for i in b:
    print(i[0],i[1])
