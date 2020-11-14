#못풀었음
#99프로에서 런타임 에러뜸
import sys
a=[list(map(str,sys.stdin.readline().split())) for i in range(int(sys.stdin.readline()))]
b=sorted(a,key=lambda x:(int(x[1]),x[0]))
if b[0][1]!=b[1][1]:
    print(b[-1][0])
else:
    print(b[0][0])
