#별찍기 - 12
a=int(input())
for i in range(1,2*a):
    if i<=a:
        print(" "*(a-i)+"*"*(i))
    elif i>a:
        print(" "*(i-a)+"*"*(2*a-i))
