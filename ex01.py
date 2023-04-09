import sys

def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
    else:
        init(node * 2, start, (start + end) // 2)
        init(node * 2 + 1, (start + end) // 2 + 1, end)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def segment_compare(node, start, end, left, right):
    if left > end or right < start:
        return 2e9
    
    if start >= left and right >= end:
        return tree[node]
    
    return min(segment_compare(node * 2 , start, (start + end) // 2, left, right), segment_compare(node * 2 + 1 , (start + end) // 2 + 1, end, left, right))

def update(node, start, end, index, value):
    if start > index or end < index:
        return

    if start == end:
        tree[node], nums[start] = value, value
    elif start != end:
        update(node * 2, start, (start + end) // 2, index, value)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, value)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
tree = [0] * (N * 4)
init(1, 0, N - 1)
for _ in range(int(sys.stdin.readline())):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        nums[b - 1] = c
        update(1, 0, N - 1, b - 1, c)
    elif a == 2:
        result = segment_compare(1, 0, N - 1, b - 1, c - 1)
        print(result)
