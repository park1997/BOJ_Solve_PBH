# 수찾기
import sys
a=int(sys.stdin.readline())
a_l=list(map(int,sys.stdin.readline().split()))
b=int(sys.stdin.readline())
b_l=list(map(int,sys.stdin.readline().split()))
a_l.sort()
for i in b_l:
    x=0
    y=len(a_l)-1
    while x<=y:
        mid_xy=(x+y)//2
        if a_l[mid_xy]<i:
            x=mid_xy+1
        elif a_l[mid_xy]>i:
            y=mid_xy-1
        elif a_l[mid_xy]==i:
            print(1)
            break
        else:
            print(0)
            break

        if x>y:
            print(0)
            break
