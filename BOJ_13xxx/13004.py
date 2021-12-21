# 방 배정
from math import ceil
a,b=map(int,input().split())
girl_man_1,girl_3,man_3,girl_5,man_5=0,0,0,0,0
for i in range(a):
    sex,grade=map(int,input().split())
    if grade<3:
        girl_man_1+=1
    elif grade>2 and grade<5 and sex==0:
        girl_3+=1
    elif grade>2 and grade<5 and sex==1:
        man_3+=1
    elif grade>4 and sex==0:
        girl_5+=1
    elif grade>4 and sex==1:
        man_5+=1
print(ceil(girl_man_1/b)+ceil(girl_3/b)+ceil(man_3/b)+ceil(girl_5/5)+ceil(man_5/b))
