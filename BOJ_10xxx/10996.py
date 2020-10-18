a=int(input())
if a==1:
    print("*")

else:
    if a%2==1:
        b="* "*(a//2) +"*"
        c=" *"*(a//2)

    else:
        b="* "*(a//2)
        c=" *"*(a//2)

    for i in range(a):
        print(b)
        print(c)
