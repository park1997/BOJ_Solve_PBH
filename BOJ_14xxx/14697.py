# 방 배정하기
a,b,c,T = map(int,input().split())
def R(a,b,c):
    for a1 in range(101):
        for b1 in range(101):
            for c1 in range(101):
                if a*a1 + b*b1 + c*c1 == T:
                    return print(1)
    return print(0)
R(a,b,c)
