import sys
a=sys.stdin.readline().rstrip()
num=[int(i) for i in a]
if ("0" not in a) or (sum(num)%3!=0):
    print(-1)
else:
    num=sorted(num,reverse=True)
    print(*num,sep="")
