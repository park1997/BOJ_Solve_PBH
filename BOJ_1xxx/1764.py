# 듣보잡
import sys
a,b=map(int,sys.stdin.readline().split())
see_hear=[]
s_h=[]
cnt=0
for i in range(a+b):
    see_hear.append(sys.stdin.readline())
see_hear.sort()
i=0
while i<a+b-1:
    if see_hear[i]==see_hear[i+1]:
        s_h.append(see_hear[i])
        i+=2
    else:
        i+=1
print(len(s_h))
for i in s_h:
    print(i,end='')