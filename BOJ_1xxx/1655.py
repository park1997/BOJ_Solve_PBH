# 가운데를 말해요
from sys import stdin
import heapq
input = stdin.readline
def heap_solution(min_heap, max_heap, target):
    # max_heap의 루트 노드가 중간값
    # max_heap의 루트는 항상 min_heap의 루트보다 같거나 작아야 한다
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -target)
    else:
        heapq.heappush(min_heap, target)
    if min_heap and -max_heap[0] > min_heap[0]:
        max_insert = -heapq.heappop(min_heap)
        min_insert = -heapq.heappop(max_heap)
        
        heapq.heappush(max_heap, max_insert)
        heapq.heappush(min_heap, min_insert)

n = int(input().rstrip())
min_heap, max_heap = [], []
for step in range(n):
    num = int(input().rstrip())
    
    heap_solution(min_heap, max_heap, num)
    print(-max_heap[0])