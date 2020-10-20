a=int(input())
count=0
for i in range(a):
    b=list(input())
    for j in range(len(b)):
        if j!=len(b)-1:
            if b[j] == b[j+1]:
                pass
            elif b[j] in b[j+1: ]:
                break
        else:
            count +=1

print(count)
