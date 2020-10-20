a, b, v = map(int, input().split())
ls = 0
if (v - b) % (a - b) != 0:
    ls = ((v - b) // (a - b)) + 1
else:
    ls = ((v - b) // (a - b))
print(ls)
