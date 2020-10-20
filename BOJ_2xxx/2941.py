a=input()
b=['c=','c-','dz=','d-','lj','nj','s=','z=']
count=0
for i in range(8):
    if b[i] in a:
        a= a.replace(b[i],'#')

print(len(a))
