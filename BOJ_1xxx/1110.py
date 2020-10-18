a=int(input())
counter = 0
b=a #=> b값을 고정시켜 버리고 while문 돌려버리기
while True:
    counter+=1
    a=((a%10)*10)+(a//10+a%10)%10
    if a == b:
        break

print(counter)


#(내가 만들어낸 오류)
#a=int(input())
#counter = 0
#c=0
#while True:
#    counter+=1
#    c=((a%10)*10)+(a//10+a%10)%10
#    if a == c:
#        break
#    else:
#        a==c
#
#print(counter)
#
#
#(a랑 c랑 같아질수가 없음)
