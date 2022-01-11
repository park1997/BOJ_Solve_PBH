# 부분 합
import sys
a,b=map(int,sys.stdin.readline().split())
c=list(map(int,sys.stdin.readline().split()))
start=0
end=1
s_e=c[start]+c[end]
result=[]
while 1:
    try:
        if s_e<b:
            end+=1
            s_e+=c[end]
        if s_e>=b:
            result.append(end-start+1)
            s_e-=c[start]
            start+=1
    except:
        break
if len(result)==0:
    print(0)
else:
    print(min(result))
