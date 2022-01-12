import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(N)]

for g in graph:
    print(g)