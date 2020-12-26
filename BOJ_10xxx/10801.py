# 카드게임
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a_c=0
b_c=0
for i in range(10):
    if a[i]<b[i]:
        b_c+=1
    elif a[i]>b[i]:
        a_c+=1
if a_c==b_c:
    print("D")
elif a_c>b_c:
    print("A")
else:
    print("B")
