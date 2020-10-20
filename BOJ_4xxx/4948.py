import math
number = [x for x in range(1,246913)]
number.insert(0,1)
for i in range(2,246913):
    j=2
    while 246912>=i*j:
        number[i*j]=1
        j+=1
a=int(input())
while a!=0:
    count=0
    for i in range(a+1,2*a+1):
        if number[i]!=1:
            count += 1
    print(count)
    a=int(input())
