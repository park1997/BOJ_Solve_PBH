a=input()
b=[0]*26
for i in range(97,123):
    b[i-97]+=a.count(chr(i))
print(*b)
