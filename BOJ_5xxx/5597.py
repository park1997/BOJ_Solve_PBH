# 과제 안 내신분..?
a=[0]*31
for i in range(28):
    a[int(input())]+=1
print(a[1:].index(0)+1)
print(a[a[1:].index(0)+2:].index(0)+1+a[1:].index(0)+1)