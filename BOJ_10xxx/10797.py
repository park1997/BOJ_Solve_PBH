# 10부제
a=int(input())
b=list(map(int,input().split()))
count=0
for i in b:
    if i==a:
        count+=1
print(count)