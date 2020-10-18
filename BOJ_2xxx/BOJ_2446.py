a=int(input())

for i in range(2*a-1):
    if a-1>i:
        print(" "*i + "*"*(2*a-2*i-1))
    elif a-1==i:
        print(" "*i + "*")
    else:
        print(" "*((2*a-1)-(i-2)-3) + "*"*(2*i-2*(a-1)+1))
