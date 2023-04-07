import sys

def init(node, start,end):
    if start == end:
        segment_tree[node] = nums[start]
        return nums[start]
    else:
        segment_tree[node] = init(node * 2, start,(start + end) // 2) * init(node * 2 + 1, (start + end) // 2 + 1, end)
        return segment_tree[node]

def update(node, start, end, index, value):
    if end < index or index < start:
        return

    if start==end:
        segment_tree[node] = value
        return

    update(node * 2, start, (start + end) // 2, index, value)
    update(node * 2 + 1, (start + end) // 2 + 1, end, index, value)
    segment_tree[node] = (segment_tree[node * 2] * segment_tree[node * 2 + 1]) % 1000000007

def segment_mul(start,end,node,left,right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return segment_tree[node]
    mid=int((start+end)/2)
    return (segment_mul(start,mid,node*2,left,right)*segment_mul(mid+1,end,node*2+1,left,right))%1000000007




N, M, K = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(N)]
segment_tree=[0] * (N * 4)

init(1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        nums[b - 1] = c
        update(1, 0, N - 1, b - 1, c)
    else:
        result = segment_mul(0, N - 1, 1, b - 1, c) 
        print(result)