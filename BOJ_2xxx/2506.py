#점수계산
a=int(input())
b=list(map(int,input().split()))
count=0
num=0
for i in b:
    if i==1:
        num+=1
        count+=num
    else:
        num=0
print(count)
