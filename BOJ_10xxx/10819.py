# 차이를 최대로
from itertools import permutations
a=int(input())
b=list(map(int,input().split()))
result=list(permutations(b,a))
num=[]
for i in result:
    sutja=0
    for j in range(len(i)-1):
        sutja+=abs(i[j]-i[j+1])
    num.append(sutja)
print(max(num))