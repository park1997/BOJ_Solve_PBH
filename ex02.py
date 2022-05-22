import sys
N,M = map(int,sys.stdin.readline().split())
l = list(map(int,sys.stdin.readline().split()))
l2 = [l[i+1]-l[i] for i in range(N-1)]
l2.sort()
print(sum(l2[:N-M]))
