#귀여운 라이언
#처음엔 투포인터로 접근 하였지만 enumerate를이용한 접근으로 풀어보았다
import sys
a,b=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
if nums.count(1)<b:
    print(-1)
else:
    lion=[i for i,j in enumerate(nums) if j==1]
    print(min((lion[b-1+k]-lion[k]+1) for k in range(len(lion)-b+1)))
