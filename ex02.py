import heapq

q = []

heapq.heappush(q, [2,2,3])
heapq.heappush(q, [1,2,3])
heapq.heappush(q, [3,2,3])
heapq.heappush(q, [1,4,3])
heapq.heappush(q, [5,2,3])
heapq.heappush(q, [1,6,3])

while q:
    cnt, x, y = heapq.heappop(q)
    if 벽
        heapq.heappush(q, [cnt +1 , nx ,ny ])
        
    print(cnt,x,y)
