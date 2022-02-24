# 가장 긴 증가하는 부분 수열 2
import sys
import bisect
n=int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
result=[arr[0]]
for i in range(1,n):
    if result[-1]<arr[i]:
        result.append(arr[i])
    else:
        idx = bisect.bisect_left(result,arr[i])
        result[idx] = arr[i]
print(len(result))