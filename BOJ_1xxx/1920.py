# 수찾기 
import sys
a=int(sys.stdin.readline())
a_l=set(map(int,sys.stdin.readline().split()))
b=int(sys.stdin.readline())
b_l=list(map(int,sys.stdin.readline().split()))
for i in b_l:
    if i in a_l:
        print(1)
    else:
        print(0)