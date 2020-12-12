#주사위게임
a=int(input())
result=[]
for i in range(a):
    b=list(map(int,input().split()))
    if b[0]==b[1] and b[1]==b[2] and b[0]==b[2]:
        result.append(10000+b[0]*1000)
    elif b[0]==b[1] or b[0]==b[2] or b[1]==b[2]:
        b.sort()
        if b.count(b[0])==2:
            result.append(1000+b[0]*100)
        else:
            result.append(1000+b[2]*100)
    else:
        b.sort()
        result.append(b[2]*100)
print(max(result))
