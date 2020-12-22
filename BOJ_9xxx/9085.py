# 더하기
a=int(input())
for i in range(a):
    b=int(input())
    b_l=list(map(int,input().split()))
    print(sum(b_l))
