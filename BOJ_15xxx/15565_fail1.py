#귀여운 라이언
#투포인터 알고리즘을 사용하였지만 시간초과가 일어난다.
import sys
a,b=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
s=0
e=0
result=[]
while 1:
    try:
        if nums[s:e+1].count(1)==b:
            result.append(e-s)
            s+=1
        else:
            e+=1
        if e==a:
            break
    except :
        break
try:
    print(min(result)+1)
except :
    print(-1)
