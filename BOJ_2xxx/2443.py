# 별 찍기 - 6
a=int(input())
for i in range(a,0,-1):
    print(" "*(a-i)+"*"*(2*i-1))