#상수
a,b=map(int,input().split())
a_r = (a//100) +((a%100)-(a%10)) + (a%10)*100
b_r = (b//100) +((b%100)-(b%10)) + (b%10)*100
if a_r < b_r:
    print(b_r)
else:
    print(a_r)
