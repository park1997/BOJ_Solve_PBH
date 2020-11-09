#팩토리얼 0의 개수
import math
import sys
a=int(sys.stdin.readline())
b=str(math.factorial(a))[::-1]
count=0
if '0' in b:
    c=b.index("0")
    while c+1<=len(b):
        if b[c+1]=='0':
            count+=1
            c+=1
        else:
            break
    print(count+1)
else:
    print(0)
