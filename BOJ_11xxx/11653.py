#소인수 분해
import sys
a=int(sys.stdin.readline())
b=2
while a!=1:
    if a%b==0:
        a=a//b
        print(b)
    else:
        b+=1
