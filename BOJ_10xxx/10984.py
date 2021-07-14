for i in range(int(input())):
    x=0
    y=0
    for j in range(int(input())):
        a,b=map(float,input().split())
        x+=a
        y+=a*b
    print("{} {:.1f}".format(int(x),y/x))