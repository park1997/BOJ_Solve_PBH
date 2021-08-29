# 숫자 카드
num1=int(input())
a=set(map(int,input().split()))
num2=int(input())
b=list(map(int,input().split()))
for i in b:
    if i in a:
        print(1,end=" ")
    else:
        print(0,end=" ")