# 이진수 변환
a= int(input())
n = 0
result = ""
while 1:
    b=2**n
    if a<b:
        n-=1
        break
    n+=1
for i in range(n,-1,-1):
    if a-(2**i)>=0:
        result+='1'
        a-=2**i
    else:
        result+='0'
print(result)