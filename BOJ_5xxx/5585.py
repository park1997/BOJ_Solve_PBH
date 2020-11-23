#거스름돈
a=int(input())
a=1000-a
b=[500,100,50,10,5,1]
count=0
for i in b:
    if i>a:
        continue
    else:
        count+=a//i
        a=a-i*(a//i)
    if a==0:
        break
print(count)
