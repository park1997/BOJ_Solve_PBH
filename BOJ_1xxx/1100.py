# 하얀 칸
a=[input() for i in range(8)]
count=0
for i in range(8):
    for j in range(4):
        if i%2==0 and a[i][2*j]=="F":
            count+=1
        elif i%2!=0 and a[i][2*j-1]=='F':
            count+=1
print(count)
