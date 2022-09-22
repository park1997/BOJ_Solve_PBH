from re import L
import sys
from heapq import heappush,heappop
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
M = int(input())

dic = defaultdict(list)

for _ in range(M):
    start,depart,cost = map(int,input().split())
    dic[start].append((cost,depart))


start,depart = map(int,input().split()) 

def dijkstra(x):

    h = []
    heappush(h,[0,x])
    visited = [float('inf')]*(N+1)

    visited[x] = 0

    while h :
        
        curr_cost,curr_node = heappop(h)
        if curr_cost > visited[curr_node]:
            continue

        for next_cost,next_node in dic[curr_node]:
            sum_cost = next_cost + curr_cost

            if sum_cost<visited[next_node]:
                visited[next_node] =  sum_cost
                heappush(h,[sum_cost,next_node])

    return visited
answer = dijkstra(start)
print(answer[depart])
