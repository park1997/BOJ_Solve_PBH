# 상금헌터
a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    sum_b=0
    sum_c=0
    if b==1:
        sum_b=5000000
    elif 2<=b<4:
        sum_b=3000000
    elif 4<=b<7:
        sum_b=2000000
    elif 7<=b<11:
        sum_b=500000
    elif 11<=b<16:
        sum_b=300000
    elif 16<=b<22:
        sum_b=100000
    if c==1:
        sum_c=5120000
    elif 2<=c<4:
        sum_c=2560000
    elif 4<=c<8:
        sum_c=1280000
    elif 8<=c<16:
        sum_c=640000
    elif 16<=c<32:
        sum_c=320000
    print(sum_b+sum_c)
