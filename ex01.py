def bi(a):
    n=0
    result=''
    while 1:
        b=2**n
        if a-b<0:
            n-=1
            break
        n+=1
    for i in range(n,-1,-1):
        b=2**i
        if a-b >=0:
            result+='1'
            a-=b
        else:
            result+='0'
    return result
n=bi(int(input()))[::-1]
ans = 0
for i,j in enumerate(n):
    if j=='1':
        ans+=2**(len(n)-int(i)-1)
print(ans)