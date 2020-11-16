#막대기
a=int(input())
b=[64,32,16,8,4,2,1]
count=0
for i in b:
    if a<i:
        continue
    else:
        a-=i
        count+=1
        if a==0:
            break
print(count)
