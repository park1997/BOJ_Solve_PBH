num=0
result=[]
for i in range(4):
    a,b=map(int,input().split())
    num-=a
    num+=b
    result.append(num)
print(max(result))