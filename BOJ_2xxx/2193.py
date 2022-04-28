# 이친수
N = int(input())
a0 = 0
a1 = 1
if N ==1:
    print(1)
else:
    for i in range(N-1):
        result0 = a1 + a0
        result1 = a0
        a0  = result0
        a1  = result1
    print(a0+a1)