# 에라토스테네스의 체
a,b=map(int,input().split())
list_1=[i for i in range(1,a+1)]
list_2=[i for i in range(1,a+1)]
num=1
count=0
while count!=b:
    num+=1
    list_1=list_2
    for i in list_1:
        if i%num==0:
            list_2.remove(i)
            count+=1
            if count==b:
                print(i)
                break