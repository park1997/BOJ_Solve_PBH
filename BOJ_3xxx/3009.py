a_x=[]
a_y=[]
for i in range(3):
    b,c=map(int,input().split())
    a_x.append(b)
    a_y.append(c)
for i in a_x:
    if a_x.count(i) ==2 :
        continue
    else:
        x=i
for i in a_y:
    if a_y.count(i)==2:
        continue
    else:
        y=i
print("{} {}".format(x,y))
