import heapq
import sys
heap=[]
for i in range(int(sys.stdin.readline())):
    b=int(sys.stdin.readline())
    if b==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,b)
