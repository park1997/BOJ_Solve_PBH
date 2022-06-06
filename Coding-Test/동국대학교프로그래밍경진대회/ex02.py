a,b=map(int,input().split())
count = [0]*10
for i in range(a+1,b):
    for j in list(str(i)):
        count[int(j)]+=1
print(*count)
