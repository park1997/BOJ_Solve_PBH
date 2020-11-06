#요세푸스 문제
import sys
a,b=map(int,sys.stdin.readline().split())
a_list=list(range(1,a+1))
num=[]
c=b-1
while 1:
    num.append(a_list.pop(c))
    if len(a_list)==0:
        break
    c=(c+b-1)%len(a_list)
print("<",end="")
print(*num,sep=", ",end=">")
