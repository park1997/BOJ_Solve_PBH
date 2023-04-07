import sys

def segment_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if start >= left and right >= end:
        return segment_tree[node]
    return segment_sum(node * 2, start, (start + end) // 2, left, right) + segment_sum(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

def update(index, diff):
    while index >= 1:
        segment_tree[index] += diff
        index //= 2

N, M = map(int, sys.stdin.readline().split())
nums = [0] * (N)
segment_tree = [0] * (N * 4)

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0:
        result = segment_sum(1, 0, N - 1, a - 1, b - 1)
        print(result)
    elif a == 1:
        diff = c - nums[b - 1]
        nums[b - 1] = c
        update(1, 0, N - 1, b - 1, diff)

    
    

