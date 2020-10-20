a=int(input())
if a ==1:
    print(1)
else:
    b=1
    c=1
    while a >= 2:
        a -= b*6
        b +=1
        c +=1
    print(c)
