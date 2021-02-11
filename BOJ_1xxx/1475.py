# 방번호 
a=input()
result_1=0
result=[0]*10
for i in a:
    if i=='6' or i=='9':
        result_1+=1
    else:
        result[int(i)]+=1
if result_1<=max(result)*2:
    print(max(result))
else:
    if result_1%2==0:
        print(result_1//2)
    else:
        print((result_1//2)+1)