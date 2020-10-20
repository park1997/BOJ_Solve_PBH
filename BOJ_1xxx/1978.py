a = int(input())
b = list(map(int,input().split()))
count = 0
count_1 =0

for i in list(b):
    if i==1:
        continue
    for j in range(2,i):
        if i%j==0:
            count += 1
            break
for k in list(b):
    if k ==1:
        count_1 +=1

print(a-count-count_1)
