#윷놀이
b=["A","B","C","D","E"]
for i in range(3):
    a=list(map(int,input().split()))
    print(b[a.count(0)-1])
