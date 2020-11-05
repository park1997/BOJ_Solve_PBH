import sys
a=int(sys.stdin.readline())
b=[]
for i in range(a):
    c=list(map(str,sys.stdin.readline().split()))
    if c[0] == 'push':
        b.append(c[1])
    elif c[0] == 'pop':
        if len(b) == 0:
            print(-1)
        else:
            print(b.pop())
    elif c[0] == 'size':
        print(len(b))
    elif c[0] == 'empty':
        if len(b)==0:
            print(1)
        else:
            print(0)
    elif c[0] == 'top':
        if len(b)==0:
            print(-1)
        else:
            print(b[-1])
