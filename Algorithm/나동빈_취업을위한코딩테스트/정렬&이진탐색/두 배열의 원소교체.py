N,K= map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()
for i in range(K):
    if a[i] < b[-1-i]:
        a[i] = b[-i-1]
    else:
        break
print(sum(a))