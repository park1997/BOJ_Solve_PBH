import sys
import heapq
def binary_search(graph,target):
    x = 0
    y = len(graph) - 1
    while x<=y:
        mid = (x+y) // 2
        if H[mid] < target:
            x = mid + 1
        else:
            y = mid -1
    graph.insert(x,target)
    return graph

N,M = map(int,sys.stdin.readline().split())
H = list(map(int,sys.stdin.readline().split()))
H.sort()
cnt = 0
while 1:
    cnt += 1
    r = H.pop(-1) // 2
    H = binary_search(H,r)
    if cnt == M:
        print(sum(H))
        break