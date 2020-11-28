#음계
a=list(map(int,input().split()))
a_1=[1,2,3,4,5,6,7,8]
a_2=[8,7,6,5,4,3,2,1]
if a==a_1:
    print("ascending")
elif a==a_2:
    print("descending")
else:
    print("mixed")
