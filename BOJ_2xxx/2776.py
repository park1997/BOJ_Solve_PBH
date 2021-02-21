# 암기왕
for i in range(int(input())):
    a=int(input())
    a_l=set(map(int,input().split()))
    b=int(input())
    b_l=list(map(int,input().split()))
    for j in b_l:
        if j in a_l:
            print(1)
        else:
            print(0)