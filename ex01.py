a = list(map(int,input().split()))
b = [i*2 for i in a]
for i in b:
    a.append(i)
print(*b)
