#랜선자르기
#이분탐색
#Binary Research
import sys
a,b=map(int,sys.stdin.readline().split())
c=[int(sys.stdin.readline()) for i in range(a)]
n_1=1
n_2=max(c)
while n_1<=n_2:
    d=0
    mid=(n_1+n_2)//2
    for i in c:
        d+=i//mid
    if d>=b:
        n_1=1+mid
    else:
        n_2=mid-1
print(n_2)
