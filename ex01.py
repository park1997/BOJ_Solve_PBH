import sys
a,b=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
if nums.count(1)<b:
    print(-1)
else:
    lion=[i for i,j in enumerate(nums) if j==1]
    print(min((lion[b-1+k]-lion[k]+1) for k in range(len(lion)-b+1)))
