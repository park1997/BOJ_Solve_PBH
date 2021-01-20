# 완전제곱수
import math
a=int(input())
b=int(input())
a_1=int(math.sqrt(a))-1
b_1=int(math.sqrt(b))+1
result=[]
for i in range(a_1,b_1):
    if a<=i*i<=b:
        result.append(i*i)
if len(result)==0:
    print(-1)
else:        
    print(sum(result))
    print(result[0])