n = int(input())
l = list(map(int,input().split()))
j = list(map(int,input().split()))
h = 0
f = 0
for i in range(n):
    h += l[i]
    f += j[i]
    if h > 100:
        h -= l[i]
        f -= j[i]
        break;
    print(h,f)
print(f)
