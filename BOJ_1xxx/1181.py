import sys
a=int(sys.stdin.readline())
b=list(set([sys.stdin.readline() for i in range(a)]))
b_1 = []
for i in b:
    b_1.append([len(i),i])
b_1.sort()
for i in b_1:
    print(i[1],end="")
