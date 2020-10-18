a=[]
b=[]
for i in range(3):
    a.append(int(input()))
a=min(a)
for i in range(2):
    b.append(int(input()))
b=min(b)

print(a+b-50)
