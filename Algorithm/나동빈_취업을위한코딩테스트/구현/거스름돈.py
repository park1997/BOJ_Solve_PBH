n = 1260

coin = [500,100,50,10]
cnt = 0
for c in coin:
    cnt += n//c
    n -= c*(n//c)
print(cnt)