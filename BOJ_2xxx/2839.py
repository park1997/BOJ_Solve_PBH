a=int(input())
b=a
count =0
if a==4 or a==7:
    print(-1)
else:
    for i in range((a//5),-1,-1):
        a= a-(5*i)
        if a%3 ==0 :
            count =(a//3) +i
            break
        else:
            a=b
    print(count)
