#요세푸스 문제 0
import sys
a,b=map(int,sys.stdin.readline().split())
c=[i for i in range(1,a+1)]
d=[]
e=b-1
while 1:
    d.append(c.pop(e))
    if len(c)==0:
        break
    e=(e+b-1)%len(c)
print("<",end="")
print(*d,sep=", ",end=">")
